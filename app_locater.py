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


For the above mentioned text of Feature file generate a locator file in python.
locator file can be defined as follows : Python defines the locators (like XPath, CSS selectors, etc.) for various elements on the web page that will be interacted with during testing.

Follow the below instructions for completing the task
1. Go through and understand the text of the feature file to identify all the web elements that need locators.
2. Determine all the web elements that will be interacted with based on the steps in the feature file.
3. Use selenium to navigate to visit the URL and identify the elements.Use the Selenium WebDriver to find and test the locators.
4. Take a screenshot of every page visited during the locator identification process.Use these screenshots to verify the correctness of the locators.
5. Save the locators as JSON in the current directory with the name of ``
                 
Use the following steps in order to verify if the locator file is properly implemented or not
1. Ensure that all locators uniquely identify their respective elements.
2. Test each locator using a simple Python script to confirm they work.

Test each locator using a simple Python script to confirm they work.
Important instructions:
1. assume selenium and behave to be pre-installed
2. assume chromedriver is present in the current directory
3. while making feature file use python script and not terminal commands
""")