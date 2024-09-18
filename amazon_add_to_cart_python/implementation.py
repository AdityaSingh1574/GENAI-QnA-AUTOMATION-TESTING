
import unittest
from step_definitions import AmazonSteps

class TestAmazonCart(unittest.TestCase):
    def setUp(self):
        self.amazon = AmazonSteps()

    def tearDown(self):
        self.amazon.close_browser()

    def test_add_book_to_cart(self):
        # Scenario: Search and Add Book to Cart
        self.amazon.open_amazon_homepage()
        self.amazon.search_for_item('Python Programming Book')
        self.amazon.select_first_item('Python Programming Book')
        self.amazon.add_to_cart()
        self.amazon.verify_item_in_cart('Python Programming Book')
        self.amazon.verify_cart_count_increase()

    def test_add_shoes_to_cart(self):
        # Scenario: Search and Add Shoes to Cart
        self.amazon.open_amazon_homepage()
        self.amazon.search_for_item('Running Shoes')
        self.amazon.select_first_item('Running Shoes')
        self.amazon.select_size_and_color()
        self.amazon.add_to_cart()
        self.amazon.verify_item_in_cart('Running Shoes')
        self.amazon.verify_cart_count_increase()

if __name__ == '__main__':
    unittest.main()
