
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

XPATHS = {
    "search_bar": "//input[@id='twotabsearchtextbox']",
    "search_button": "//input[@id='nav-search-submit-button']",
    "first_search_result": "(//div[@data-component-type='s-search-result']//h2/a)[1]",
    "add_to_cart": "//input[@id='add-to-cart-button']",
    "cart_counter": "//span[@id='nav-cart-count']",
    "size_dropdown": "//select[@id='native_dropdown_selected_size_name']",
    "color_options": "//ul[@role='radiogroup']//li",
    "cart_item_title": "//span[@class='a-truncate-cut']"
}

class AmazonSteps:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_amazon_homepage(self):
        self.driver.get("https://www.amazon.com")

    def search_for_item(self, item):
        search_bar = self.wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["search_bar"])))
        search_bar.clear()
        search_bar.send_keys(item)
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["search_button"])))
        search_button.click()

    def select_first_item(self, item):
        first_result = self.wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["first_search_result"])))
        first_result.click()

    def select_size_and_color(self):
        try:
            size_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["size_dropdown"])))
            size_dropdown.click()
            size_options = size_dropdown.find_elements(By.TAG_NAME, "option")
            if len(size_options) > 1:
                size_options[1].click()
        except:
            print("Size selection not available for this item")

        try:
            color_options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, XPATHS["color_options"])))
            if color_options:
                color_options[0].click()
        except:
            print("Color selection not available for this item")

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["add_to_cart"])))
        add_to_cart_button.click()

    def verify_item_in_cart(self, item):
        self.driver.get("https://www.amazon.com/gp/cart/view.html")
        cart_items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, XPATHS["cart_item_title"])))
        item_found = any(item.lower() in cart_item.text.lower() for cart_item in cart_items)
        assert item_found, f"{item} was not found in the cart"

    def verify_cart_count_increase(self):
        initial_count = int(self.wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["cart_counter"]))).text)
        time.sleep(2)  # Wait for the cart to update
        final_count = int(self.wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["cart_counter"]))).text)
        assert final_count > initial_count, "Cart count did not increase"

    def close_browser(self):
        self.driver.quit()
