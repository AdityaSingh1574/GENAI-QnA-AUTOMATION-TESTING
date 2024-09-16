
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_locators():
    # Load locators from JSON file
    with open("amazon_add_to_cart_updated.json", "r") as f:
        locators = json.load(f)

    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to Amazon India
        driver.get("https://www.amazon.in")

        # Test homepage locators
        homepage_locators = ["search_box", "search_button", "cart_count"]
        for name in homepage_locators:
            locator = locators[name]
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((getattr(By, locator['by']), locator['value']))
                )
                print(f"Locator '{name}' found successfully on homepage")
            except Exception as e:
                print(f"Locator '{name}' not found on homepage: {str(e)}")

        # Search for a product
        search_box = driver.find_element(By.ID, locators["search_box"]["value"])
        search_box.send_keys("shoes")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

        # Test search results page locators
        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locators["first_result"]["value"]))
            )
            print("Locator 'first_result' found successfully on search results page")
            first_result.click()
            time.sleep(2)
        except Exception as e:
            print(f"Locator 'first_result' not found on search results page: {str(e)}")

        # Test product page locators
        product_page_locators = ["add_to_cart_button", "size_dropdown", "color_options"]
        for name in product_page_locators:
            locator = locators[name]
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((getattr(By, locator['by']), locator['value']))
                )
                print(f"Locator '{name}' found successfully on product page")
            except Exception as e:
                print(f"Locator '{name}' not found on product page: {str(e)}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_locators()

print("Locator testing completed.")
