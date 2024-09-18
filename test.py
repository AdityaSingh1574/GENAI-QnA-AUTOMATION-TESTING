import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAmazonAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()

    def search_for_item(self, item_name):
        search_bar = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="twotabsearchtextbox"]')))
        search_bar.send_keys(item_name)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
        search_button.click()

    def select_first_item(self):
        first_item = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span')))
        first_item.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button"]')))
        add_to_cart_button.click()

    def get_cart_count(self):
        cart_counter = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav-cart-count"]')))
        return int(cart_counter.text)

    def test_add_book_to_cart(self):
        # Test case: Search and add 'Book' to the cart
        initial_cart_count = self.get_cart_count()
        self.search_for_item("Book")
        self.select_first_item()
        self.add_to_cart()
        
        new_cart_count = self.get_cart_count()
        self.assertEqual(new_cart_count, initial_cart_count + 1, "Cart count did not increase by 1 for Book")

    def test_add_shoes_to_cart(self):
        # Test case: Search and add 'Shoes' to the cart
        initial_cart_count = self.get_cart_count()
        self.search_for_item("Shoes")
        self.select_first_item()
        self.add_to_cart()
        
        new_cart_count = self.get_cart_count()
        self.assertEqual(new_cart_count, initial_cart_count + 1, "Cart count did not increase by 1 for Shoes")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
