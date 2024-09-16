from interpreter import interpreter
from dotenv import load_dotenv
import os
load_dotenv()


interpreter.auto_run = True
interpreter.llm.model = "openai/claude-3-5-sonnet"
interpreter.llm.api_base = 'http://localhost:4000'
interpreter.llm.supports_vision = True
interpreter.llm.supports_functions = True
interpreter.llm.temperature = 0.1


interpreter.chat("""
Feature: MultiSteps Form Automation with Screenshot and Screen Recording
As a user, I want to fill out a multi-step form on https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_form_steps
So that I can complete the registration process

Scenario: User Fills and Completes the Multi-Step Form
Given user opens the multiStepForm
When user fills in the "First name" field with 'Aditya'
And user fills in the "Last name" field with 'Singh'
And user fills in the "E-mail" field with 'abc@bbc.com'
And user fills in the "Phone" field with '+123456789'
And user fills in the "dd" field for birth date with '01'
And user fills in the "mm" field for birth month with '01'
And user fills in the "yyyy" field for birth year with '2007'
And user fills in the "Username" field with 'aditya1574'
And user fills in the "Password" field with '123@bbc'
And user clicks the "Next" button to proceed to the next step
Then user should see the next step of the form
When user completes all steps of the form
And user clicks the "Submit" button
Then the form should be successfully submitted
And a screenshot of the completed form should be captured
And a screen recording of the form filling process should be saved

For the above mentioned text of Feature file generate a locator file in python.
locator file can be defined as follows : Python defines the locators (like XPath, CSS selectors, etc.) for various elements on the web page that will be interacted with during testing.

Follow the below instructions for completing the task
1. Go through and understand the text of the feature file to identify all the web elements that need locators.
2. Determine all the web elements that will be interacted with based on the steps in the feature file.
3. Use selenium to navigate to visit the URL and identify the elements.Use the Selenium WebDriver to find and test the locators.
4. Take a screenshot of every page visited during the locator identification process.Use these screenshots to verify the correctness of the locators.
5. Save the locators as JSON in the current directory with the name of `<webpage name>_<task name>.json` and store the locators in JSON file with the same name
6. Also generate a test_locators.py for testing the locators for verification
                 
Use the following steps in order to verify if the locator file is properly implemented or not
1. Ensure that all locators uniquely identify their respective elements.
2. Test each locator using a simple Python script to confirm they work.

Important instructions:
1. assume selenium and behave to be pre-installed
2. assume chromedriver is present in the current directory
3. while making feature file use python script and not terminal commands
""")