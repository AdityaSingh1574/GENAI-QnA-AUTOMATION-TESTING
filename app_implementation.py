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



Follow the below instructions for completing the task
1. Review the feature file to understand the actions that need to be performed and identify the web pages and elements involved.
2. Implementation file contains methods to interact with web elements, encapsulating the logic for different pages or components of the application.
3. Implement the steps in python using the libraries : behave, selenium, chromedriver
4. Take a screenshot of every page you visit. Use these screenshots to select elements for performing actions. Save the screenshots for reference.
5. Run `behave` in the terminal for running the step definition file


Use the following steps in order to verify if the step definition file is properly implemented or not
Check the Output:
1. Write a simple script to instantiate the implementation file and test each method to ensure they work correctly.
2. Include error handling to manage exceptions and unexpected behavior.
 
Important instructions:
1. assume selenium and behave to be pre-installed
2. assume chromedriver is present in the current directory
3. while making feature file use python script and not terminal commands                     
""")