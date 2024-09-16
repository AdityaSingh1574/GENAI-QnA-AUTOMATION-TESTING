
import time
import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_locators():
    # Load locators from JSON file
    with open("amazon_homepage_dropdown.json", "r") as f:
        locators = json.load(f)

    # Setup Chrome driver
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = uc.Chrome(options=chrome_options)

    try:
        # Navigate to Amazon India homepage
        driver.get("https://www.amazon.in")
        time.sleep(5)  # Wait for page to load

        # Test each locator
        for name, (by, value) in locators.items():
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((getattr(By, by), value))
                )
                print(f"Locator '{name}' found successfully")
                
                # If it's the dropdown menu, try selecting options
                if name == "dropdown_menu":
                    from selenium.webdriver.support.ui import Select
                    select = Select(element)
                    
                    # Select "All Categories"
                    select.select_by_visible_text("All Categories")
                    time.sleep(2)
                    driver.save_screenshot("all_categories_selected.png")
                    
                    # Select "Alexa Skills"
                    select.select_by_visible_text("Alexa Skills")
                    time.sleep(2)
                    driver.save_screenshot("alexa_skills_selected.png")
                    
                    print("Dropdown options selected successfully")
                
            except Exception as e:
                print(f"Error: Locator '{name}' not found or not interactable. Error: {str(e)}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_locators()
