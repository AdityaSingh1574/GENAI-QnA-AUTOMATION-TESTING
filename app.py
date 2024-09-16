from interpreter import interpreter
from dotenv import load_dotenv
import os
import json
load_dotenv()




interpreter.auto_run = True
interpreter.llm.model = "openai/claude-3-5-sonnet"
interpreter.llm.api_base = 'http://localhost:4000'
interpreter.llm.supports_vision = True
interpreter.llm.supports_functions = True
interpreter.llm.temperature = 0.1





# interpreter.custom_instructions = """
# 1. When taking the screen shot at every subtask save the screenshot save the screenshot in the format `subtask_<task number>` and save it in the current directory
# 2. Use the filepath for accessing the screenshot for analyzing 
# 4. Perform the task given using python and selenium, assume that they are pre-installed
# 4. If automated access is blocked in the website in the user message then quit from the process and inform the same
# """

# interpreter.llm.execution_instructions  = """You need to follow these instructions to execute the given Task:
# 1. read and analyse the message but the user and divide the whole task into subtasks
# 2. start by taking a screenshot of the webpage and store it in the current directory into the folder for every page you visit as a part of the subtasks
# 3. use the saved screenshot to identify the element where the action has to be performed, for example identify the search bar for performing the search operation in the document
# 4. analyze the the html content and try to find the correct xpath. You can Ignore tags like  <script> , <link>, <iframe>
# 5. Give an Analysis of why code failed and then proceed with re-writing.
# 6. To Verify if the Task was successfully done, check which site it has landed to maybe url or title
# 7. Use Python Selenium and assume chrome driver is already installed.
# 8. Do not use WebDriverWait function for webdriver to find elements.
# 9. Save the working code in the current directory after verifying the steps are correct.
# 10. At the end of the tasks show a confirmatory result by taking a screenshot of the same and save in the current directory
# """

interpreter.chat("""
Feature: Select preferable language on Amazon at https://www.amazon.in/
  As a user, I want to select my preferred language on Amazon

  Scenario: Select English as the preferred language
    Given user opens the language tab on Amazon homepage
    When user selects "English" from the language options
    Then the website should display in English language
    And user preferences should be updated to English

  Scenario: Select Hindi as the preferred language
    Given user opens the language tab on Amazon homepage
    When user selects "Hindi" from the language options
    Then the website should display in Hindi language
    And user preferences should be updated to Hindi         

For the above mentioned text of Feature file generate a step definition file in python.
Step definition file can be defined as follows : Python files that define the implementation of the steps described in the feature files


Make use of the file `amazon_language_selection.json` file in the current directory for getting the locators on the webpage 

Follow the below instructions for completing the task
1. Go through and understand the text of the feature file to comprehend the steps that need to be implemented.
2. Step definition file will contain the Python code that defines the steps for the feature file text
3. Implement the steps in python using the libraries : behave, selenium, chromedriver
4. Take a screenshot of every page you visit. Use these screenshots to select elements for performing actions. Save the screenshots for reference.
5. Run `behave` in the terminal for running the step definition file


Use the following steps in order to verify if the step definition file is properly implemented or not
Check the Output:
1. Behave will execute the scenario(s) in your feature file and print the output to the console.
2. If all steps pass, you'll see output indicating that all tests passed.
3. If there is an error or mismatch (e.g., a missing step definition), Behave will print an error message detailing the issue, resolve the issue and run again.
 
Important instructions:
1. assume selenium and behave to be pre-installed
2. assume chromedriver is present in the current directory
3. while making feature file use python script and not terminal commands
""")

