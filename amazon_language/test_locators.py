
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def test_locators():
    # Load locators
    with open("amazon_language_selection.json", "r") as f:
        locators = json.load(f)

    # Setup Chrome driver
    driver = webdriver.Chrome()

    try:
        # Navigate to Amazon India
        driver.get("https://www.amazon.in")

        # Test each locator
        for name, locator in locators.items():
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((getattr(By, locator["by"]), locator["value"]))
                )
                print(f"Locator '{name}' found successfully")
            except Exception as e:
                print(f"Error finding locator '{name}': {str(e)}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_locators()
