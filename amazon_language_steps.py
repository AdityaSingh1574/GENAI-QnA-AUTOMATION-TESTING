import os
import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def take_screenshot(driver, filename):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    driver.save_screenshot(f'screenshots/{filename}')
    logger.info(f"Screenshot saved: {filename}")

def setup_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        logger.error(f"Error setting up WebDriver: {str(e)}")
        raise

@given('user opens the language tab on Amazon homepage')
def step_open_amazon_homepage(context):
    try:
        context.driver = setup_driver()
        context.driver.get('https://www.amazon.in/')
        take_screenshot(context.driver, 'amazon_homepage.png')
        
        # Open language tab
        language_tab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'icp-nav-flyout'))
        )
        language_tab.click()
        take_screenshot(context.driver, 'language_tab_open.png')
    except Exception as e:
        logger.error(f"Error in opening Amazon homepage: {str(e)}")
        raise

@when('user selects "{language}" from the language options')
def step_select_language(context, language):
    try:
        # Select the specified language
        language_option = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{language}')]"))
        )
        language_option.click()
        take_screenshot(context.driver, f'{language.lower()}_selected.png')
    except Exception as e:
        logger.error(f"Error in selecting language: {str(e)}")
        raise

@then('the website should display in {language} language')
def step_verify_language_display(context, language):
    try:
        # Verify the language change
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[@class='nav-line-1' and contains(text(), '{language}')]"))
        )
        take_screenshot(context.driver, f'{language.lower()}_display.png')
    except Exception as e:
        logger.error(f"Error in verifying language display: {str(e)}")
        raise

@then('user preferences should be updated to {language}')
def step_verify_preferences(context, language):
    try:
        # Verify user preferences (this is a simplified check)
        language_tab = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'icp-nav-flyout'))
        )
        assert language in language_tab.text, f"Language preference not updated to {language}"
        take_screenshot(context.driver, f'{language.lower()}_preference.png')
    except Exception as e:
        logger.error(f"Error in verifying user preferences: {str(e)}")
        raise
    finally:
        context.driver.quit()
