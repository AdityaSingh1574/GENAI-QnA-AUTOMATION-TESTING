
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Import step definitions
from steps.step_definitions import *

def before_scenario(context, scenario):
    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    
    # Navigate to Amazon homepage
    context.driver.get("https://www.amazon.in")
    
    # Get initial cart count
    cart_counter = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATHS["cart_counter"]))
    )
    context.initial_cart_count = int(cart_counter.text)

def after_scenario(context, scenario):
    # Clean up
    if hasattr(context, 'driver'):
        context.driver.quit()

# The step definitions are already imported from step_definitions.py,
# so we don't need to redefine them here.
