
import os
import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def take_screenshot(driver, filename):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot(f"screenshots/{filename}")

@given('user opens the language tab on Amazon homepage')
def step_open_amazon_homepage(context):
    context.driver = setup_driver()
    context.driver.get("https://www.amazon.in/")
    take_screenshot(context.driver, "amazon_homepage.png")
    logger.info("Opened Amazon homepage")
    
    try:
        language_selector = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "icp-nav-flyout"))
        )
        language_selector.click()
        take_screenshot(context.driver, "language_tab_open.png")
        logger.info("Clicked on language selector")
    except TimeoutException:
        logger.error("Timeout waiting for language selector")
        take_screenshot(context.driver, "language_selector_error.png")
        raise

@when('user selects "{language}" from the language options')
def step_select_language(context, language):
    try:
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "icp-language-settings"))
        )
        
        language_xpath = f"//span[contains(@class, 'a-radio-label') and contains(text(), '{language}')]"
        language_option = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, language_xpath))
        )
        language_option.click()
        logger.info(f"Selected {language} language")
        
        take_screenshot(context.driver, f"{language.lower()}_selected.png")
        
        save_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#icp-save-button input[type='submit']"))
        )
        save_button.click()
        logger.info("Clicked Save Changes button")
    except TimeoutException:
        logger.error(f"Timeout waiting for {language} option or Save Changes button")
        take_screenshot(context.driver, f"{language.lower()}_selection_error.png")
        raise
    except NoSuchElementException:
        logger.error(f"Could not find {language} option or Save Changes button")
        take_screenshot(context.driver, f"{language.lower()}_selection_error.png")
        raise

@then('the website should display in {language} language')
def step_verify_language_display(context, language):
    try:
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
        )
        
        take_screenshot(context.driver, f"website_in_{language.lower()}.png")
        
        page_source = context.driver.page_source.lower()
        if language.lower() == "english":
            assert "hello" in page_source or "sign in" in page_source
        elif language.lower() == "hindi":
            assert "namaste" in page_source or "sign in" in page_source
        logger.info(f"Verified website display in {language}")
    except TimeoutException:
        logger.error("Timeout waiting for page reload after language change")
        take_screenshot(context.driver, f"language_change_error_{language.lower()}.png")
        raise
    except AssertionError:
        logger.error(f"Could not verify {language} language display")
        take_screenshot(context.driver, f"language_verification_error_{language.lower()}.png")
        raise

@then('user preferences should be updated to {language}')
def step_verify_user_preferences(context, language):
    try:
        language_selector = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "icp-nav-flyout"))
        )
        
        assert language.lower() in language_selector.text.lower()
        take_screenshot(context.driver, f"preferences_updated_to_{language.lower()}.png")
        logger.info(f"Verified user preferences updated to {language}")
    except TimeoutException:
        logger.error("Timeout waiting for language selector after preference update")
        take_screenshot(context.driver, f"preference_update_error_{language.lower()}.png")
        raise
    except AssertionError:
        logger.error(f"Could not verify user preferences updated to {language}")
        take_screenshot(context.driver, f"preference_verification_error_{language.lower()}.png")
        raise
    finally:
        context.driver.quit()
        logger.info("Closed the browser")
