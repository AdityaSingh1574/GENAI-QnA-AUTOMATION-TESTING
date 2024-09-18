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
# interpreter.loop = True





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

# interpreter.chat("""
# ---FEATURE-FILE-START---

# Feature: Add Items to Cart on https://www.amazon.in
# As a user, I want to search for various items on Amazon and add them to my cart

# Scenario: Search and Add Book to Cart
# Given user is on the Amazon homepage
# When user searches for 'Book' in the search box
# And user selects the first 'Book' from the search results
# And user clicks on 'Add to Cart' button
# Then the 'Book' should be added to the user's cart
# And the cart count should increase by 1

# Scenario: Search and Add Shoes to Cart
# Given user is on the Amazon homepage
# When user searches for 'Shoes' in the search box
# And user selects the first 'Shoes' from the search results
# And user selects the desired size and color
# And user clicks on 'Add to Cart' button
# Then the 'Shoes' should be added to the user's cart
# And the cart count should increase by 1


# ---FEATURE-FILE-END---

# the feature file is given between `---FEATURE-FILE-START---` and `---FEATURE-FILE-END---`
# Your task will be to implement the step definition and implementation files using the above given feature file text in PYTHON

# You can use the following instructions for generating the step definition and implementation files
# 1. Go through and understand the text of the feature file to comprehend the steps that need to be implemented.
# 2. Step definition file will contain the Python code that defines the steps for the feature file text 
# 3. the implementation file will contain the actual implementation of the test case / feature file containing the imports from step definition file.
# 4. Divide feature file big task into small steps / tasks and implement the functions for getting the steps done

# Important instructions:
# 1. Save the code for the implementation and step definition files using a simple python script, do not use terminal for writing in files.
# 2. The Xpaths given are accurate hence do not generate on your own
# 3. Do not use the chromedriver but for performing the same task you can use the library webdriver-manager, assume it to be installed


# use the following as locators as Xpaths for implementing the step definition file for accessing the element 
# The Xpaths are given between `---XPATH-START---` and `---XPATH-END---`

# ---XPATH-START---
# {
#     "search_bar" : "//*[@id="twotabsearchtextbox"]",
#     "search_button" : "//*[@id="nav-search-submit-button"]",
#     "first_search_result" : "//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span",
#     "add_to_cart" : "//*[@id="add-to-cart-button"]",
#     "cart_counter" : "//*[@id="nav-cart-count"]"
# }
# ---XPATH-END---
# """)

# interpreter.chat("""
# there is a step definition and an implementation files in the current directory with the following names
# 1. step definition file : `step_definition.py`
# 2. implementation file : `implementation.py`

# 1. Your task is to check and debug if they are working properly or not
# 2. if they are not working properly then debug them.
# 3. debug only if the current implementation throws an error 
# 4. do not try to add new features to the existing code and test and debug only the current code
# """)

interpreter.chat("""
Visit https://www.amazon.com, find the search bar and search for 'Python Books' and click on the search button, once you arrive to the search result click on the first result and once the product page loads completely, click on 'Add to Cart', take the screen shot for verification, save the code the current directory, use python, selenium and chromedriver for the same. 
""")