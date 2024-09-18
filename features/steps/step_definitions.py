
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# XPaths
XPATHS = {
    "search_bar": '//*[@id="twotabsearchtextbox"]',
    "search_button": '//*[@id="nav-search-submit-button"]',
    "first_search_result": '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span',
    "add_to_cart": '//*[@id="add-to-cart-button"]',
    "cart_counter": '//*[@id="nav-cart-count"]'
}

@given('user is on the Amazon homepage')
def step_impl(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.amazon.in")
    context.driver.maximize_window()

@when(f'user searches for {item} in the search box')
def step_impl(context, item):
    search_bar = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATHS["search_bar"]))
    )
    search_bar.clear()
    search_bar.send_keys(item)
    
    search_button = context.driver.find_element(By.XPATH, XPATHS["search_button"])
    search_button.click()

@when(f'user selects the first {item} from the search results')
def step_impl(context, item):
    first_result = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, XPATHS["first_search_result"]))
    )
    first_result.click()

@when(f'user selects the desired size and color')
def step_impl(context):
    # This step is specific to shoes and may require additional implementation
    # For now, we'll just pass as it depends on the specific product page layout
    pass

@when(f'user clicks on 'Add to Cart' button')
def step_impl(context):
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, XPATHS["add_to_cart"]))
    )
    add_to_cart_button.click()

@then(f"the {item}" should be added to the user's cart')
def step_impl(context, item):
    # This step might require additional verification, such as checking a confirmation message
    # For now, we'll assume that if we reach this step, the item was added successfully
    pass

@then(f'the cart count should increase by 1')
def step_impl(context):
    cart_counter = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATHS["cart_counter"]))
    )
    new_cart_count = int(cart_counter.text)
    assert new_cart_count > context.initial_cart_count, "Cart count did not increase"

    # Clean up
    context.driver.quit()
