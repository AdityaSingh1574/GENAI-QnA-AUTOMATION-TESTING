
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class AmazonSteps:
    def __init__(self):
        self.driver = None
        self.xpaths = {
            "search_bar": '//*[@id="twotabsearchtextbox"]',
            "search_button": '//*[@id="nav-search-submit-button"]',
            "first_search_result": '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span',
            "add_to_cart": '//*[@id="add-to-cart-button"]',
            "cart_counter": '//*[@id="nav-cart-count"]'
        }

    def setup(self):
        self.driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in PATH
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def navigate_to_amazon(self):
        self.driver.get("https://www.amazon.in")

    def search_for_item(self, item):
        search_bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpaths["search_bar"]))
        )
        search_bar.clear()
        search_bar.send_keys(item)
        search_bar.send_keys(Keys.RETURN)

    def select_first_item(self, item_type):
        first_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.xpaths["first_search_result"]))
        )
        first_item.click()

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.xpaths["add_to_cart"]))
        )
        add_to_cart_button.click()

    def verify_item_added_to_cart(self, item):
        # This is a simplified check. In a real scenario, you'd want to verify the item details.
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpaths["cart_counter"]))
        )
        assert int(cart_count.text) > 0, f"{item} was not added to the cart"

    def verify_cart_count_increased(self):
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpaths["cart_counter"]))
        )
        assert int(cart_count.text) > 0, "Cart count did not increase"

    def select_size_and_color(self):
        # This is a placeholder. In a real scenario, you'd need to locate and interact with size and color selectors.
        print("Selecting size and color (placeholder)")
        time.sleep(2)  # Simulating selection time
