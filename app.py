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
Feature: Add Items to Cart on https://www.amazon.in
As a user, I want to search for various items on Amazon and add them to my cart

Scenario: Search and Add Book to Cart
Given user is on the Amazon homepage
When user searches for 'Book' in the search box
And user selects the first 'Book' from the search results
And user clicks on 'Add to Cart' button
Then the 'Book' should be added to the user's cart
And the cart count should increase by 1

Scenario: Search and Add Shoes to Cart
Given user is on the Amazon homepage
When user searches for 'Shoes' in the search box
And user selects the first 'Shoes' from the search results
And user selects the desired size and color
And user clicks on 'Add to Cart' button
Then the 'Shoes' should be added to the user's cart
And the cart count should increase by 1              

For the above mentioned text of Feature file generate a step definition file in python.
Step definition file can be defined as follows : Python files that define the implementation of the steps described in the feature files

Follow the below instructions for completing the task
1. Go through and understand the text of the feature file and understand the steps to be done for the same
2. Step definition file will contain the Python code that defines the steps for the feature file text
3. Implement the steps in python using the libraries : behave, selenium, chromedriver
4. take a screen shot of every page you visit and using the screen shot select elements to perform action, save the screen shot for reference 
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

