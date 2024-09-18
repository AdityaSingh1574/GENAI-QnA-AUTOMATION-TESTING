import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mss
from PIL import Image

class TestMultiStepForm(unittest.TestCase):
    def setUp(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        # Navigate to the multi-step form
        self.driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_form_steps")
        self.driver.maximize_window()

        # Switch to iframe where the form is located
        self.driver.switch_to.frame("iframeResult")

    def fill_field(self, xpath, value):
        field = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        field.clear()
        field.send_keys(value)

    def click_button(self, xpath):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()

    def take_screenshot(self, step):
        screenshot_filename = f'screenshot_step_{step}.png'
        pyautogui.screenshot(screenshot_filename)
        print(f'Screenshot saved: {screenshot_filename}')

    def record_screen(self, duration):
        print("Starting screen recording...")
        with mss.mss() as sct:
            for _ in range(duration):
                sct_img = sct.grab(sct.monitors[1])
                img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
                img.save(f'screen_record_{int(time.time())}.png')
                time.sleep(1)
        print("Screen recording completed.")

    def test_form_automation(self):
        # Start screen recording (for simplicity, recording for 5 seconds)
        self.record_screen(duration=5)

        # Step 1: Fill in first and last names
        self.fill_field('//*[@id="regForm"]/div[1]/p[1]/input', 'John')  # First Name
        self.fill_field('//*[@id="regForm"]/div[1]/p[2]/input', 'Doe')   # Last Name
        self.take_screenshot('1')
        self.click_button('//*[@id="nextBtn"]')  # Next button

        # Step 2: Fill in email and phone
        self.fill_field('//*[@id="regForm"]/div[2]/p[1]/input', 'john.doe@example.com')  # Email
        self.fill_field('//*[@id="regForm"]/div[2]/p[2]/input', '1234567890')           # Phone
        self.take_screenshot('2')
        self.click_button('//*[@id="nextBtn"]')  # Next button

        # Step 3: Fill in date of birth
        self.fill_field('//*[@id="regForm"]/div[3]/p[1]/input', '15')  # Day of Birth
        self.fill_field('//*[@id="regForm"]/div[3]/p[2]/input', '07')  # Month of Birth
        self.fill_field('//*[@id="regForm"]/div[3]/p[3]/input', '1990')  # Year of Birth
        self.take_screenshot('3')
        self.click_button('//*[@id="nextBtn"]')  # Next button

        # Step 4: Fill in username and password
        self.fill_field('//*[@id="regForm"]/div[4]/p[1]/input', 'johndoe')  # Username
        self.fill_field('//*[@id="regForm"]/div[4]/p[2]/input', 'Password123')  # Password
        self.take_screenshot('4')
        self.click_button('//*[@id="nextBtn"]')  # Submit button

        # Take final screenshot and confirm submission
        self.take_screenshot('final')

        # Simulate waiting for submission process (could be replaced with actual verification logic)
        time.sleep(2)

        # Assert form submission - this could involve checking the page content or a success message
        # (depends on the form behavior after submission)
        print("Form successfully submitted.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
