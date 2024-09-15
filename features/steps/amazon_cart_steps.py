
# File: features/steps/amazon_cart_steps.py

import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('the user is on the Amazon.in homepage')
def step_user_on_amazon_homepage(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.amazon.in")
    context.driver.save_screenshot("amazon_homepage.png")

@when('the user searches for "{item}" in the search box')
def step_user_searches_for_item(context, item):
    search_box = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    context.driver.save_screenshot(f"search_results_{item}.png")

@when('the user selects the first "{item}" from the search results')
def step_user_selects_first_item(context, item):
    first_result = context.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    first_result.click()
    time.sleep(2)
    context.driver.save_screenshot(f"selected_{item}.png")

@when('the user selects the desired size and color')
def step_user_selects_size_and_color(context):
    if "Shoes" in context.scenario.name:
        size_option = context.driver.find_element(By.CSS_SELECTOR, "#native_dropdown_selected_size_name option:not(:disabled)")
        size_option.click()
        
        color_option = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name li")
        color_option.click()
        
        time.sleep(2)
        context.driver.save_screenshot("selected_size_color.png")

@when('the user clicks on "Add to Cart" button')
def step_user_clicks_add_to_cart(context):
    add_to_cart_button = context.driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()
    time.sleep(2)
    context.driver.save_screenshot("added_to_cart.png")

@then('the "{item}" should be added to the user's cart')
def step_item_added_to_cart(context, item):
    cart_count = context.driver.find_element(By.ID, "nav-cart-count")
    assert int(cart_count.text) > 0, f"{item} was not added to the cart"

@then('the cart count should increase by 1')
def step_cart_count_increased(context):
    cart_count = context.driver.find_element(By.ID, "nav-cart-count")
    current_count = int(cart_count.text)
    
    if not hasattr(context, 'previous_cart_count'):
        context.previous_cart_count = 0
    
    assert current_count == context.previous_cart_count + 1, "Cart count did not increase by 1"
    
    context.previous_cart_count = current_count

    context.driver.quit()
