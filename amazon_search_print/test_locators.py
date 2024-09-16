
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_locators():
    # Load the locators from the JSON file
    with open("amazon_india_search.json", "r") as f:
        locators = json.load(f)

    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to Amazon India
        driver.get("https://www.amazon.in")

        # Test search box locator
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((getattr(By, locators["search_box"]["by"]), locators["search_box"]["value"]))
        )
        assert search_box.is_displayed(), "Search box is not visible"

        # Test search button locator
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((getattr(By, locators["search_button"]["by"]), locators["search_button"]["value"]))
        )
        assert search_button.is_displayed(), "Search button is not visible"

        # Perform a search
        search_box.send_keys("Test")
        search_button.click()

        # Test search results locator
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((getattr(By, locators["search_results"]["by"]), locators["search_results"]["value"]))
        )
        assert len(search_results) > 0, "No search results found"

        print("All locators are working correctly!")

    except Exception as e:
        print(f"An error occurred while testing locators: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_locators()
