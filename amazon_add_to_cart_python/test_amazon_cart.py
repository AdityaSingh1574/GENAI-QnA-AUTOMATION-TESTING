
import pytest
from amazon_add_to_cart_python.amazon_steps import AmazonSteps

@pytest.fixture(scope="module")
def amazon():
    steps = AmazonSteps()
    steps.setup()
    yield steps
    steps.teardown()

def test_search_and_add_book_to_cart(amazon):
    amazon.navigate_to_amazon()
    amazon.search_for_item("Book")
    amazon.select_first_item("Book")
    amazon.add_to_cart()
    amazon.verify_item_added_to_cart("Book")
    amazon.verify_cart_count_increased()

def test_search_and_add_shoes_to_cart(amazon):
    amazon.navigate_to_amazon()
    amazon.search_for_item("Shoes")
    amazon.select_first_item("Shoes")
    amazon.select_size_and_color()
    amazon.add_to_cart()
    amazon.verify_item_added_to_cart("Shoes")
    amazon.verify_cart_count_increased()

if __name__ == "__main__":
    pytest.main([__file__])
