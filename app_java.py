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


# interpreter.system_message = """
# You are a helpful assistant and You will be given a user story and your task will be to generate new tasks on the basis of the given user story in JSON format
# The user story will be in the following format
# 1. it will be a list of instructions in gherkin syntax
# 2. the terms enclosed between < and > are placeholder and can take value as stated in the `Example` section
# 3. Find the value for the placeholder for can be found in the `Example` section with the name of the placeholder mentioned as column name
# """

# interpreter.llm.execution_instructions = """You can use the below instructions in order perform the task:
# 1. go through the user story and understand which are the placeholders and which are the values for the given placeholders
# 2. generate tasks from the given user story by replacing the placeholders with values as given in the `Example` section
# 3. cover all the examples which are given in the  `Example` section 
# 4. only the placeholder will be replaced by a value and everything else in in the task should remain same.
# """

# interpreter.chat("""
# Feature: Add Books in the cart from Amazon on https://www.amazon.in/
# As a user, I want to select my preferred language on Amazon

# Scenario: Select English as the preferred language
# Given user opens the language tab on Amazon homepage
# When user selects "English" from the language options
# Then the website should display in English language
# And user preferences should be updated to English

# Scenario: Select Hindi as the preferred language
# Given user opens the language tab on Amazon homepage
# When user selects "Hindi" from the language options
# Then the website should display in Hindi language
# And user preferences should be updated to Hindi

# Your task is to follow the instructions below and k:
# 1. visit the URL as stated in the above feature file
# 2. using python, selenium, chromedriver or any other tools first extract the xpaths of the sections of the website which needs to be visited
# 3. check if the xpath extracted is correct or not by
# 3. store the xpaths as json in the current directory with the name `<website_name>.json`

# """)

# interpreter.chat("""
# Feature: Add Books in the cart from Amazon on https://www.amazon.in/
# As a user, I want to select my preferred language on Amazon

# Scenario: Select English as the preferred language
# Given user opens the language tab on Amazon homepage
# When user selects "English" from the language options
# Then the website should display in English language
# And user preferences should be updated to English

# Scenario: Select Hindi as the preferred language
# Given user opens the language tab on Amazon homepage
# When user selects "Hindi" from the language options
# Then the website should display in Hindi language
# And user preferences should be updated to Hindi


# follow the instructions in order to complete the task:
# 1. First, make sure you have a Maven or Gradle project set up with the following dependencies Cucumber Java, Cucumber JUnit, Selenium Java, JUnit and more if required
# 2. Generate the pom.xml  for the maven project
# 3. generate the proper directory structure for the maven project and generate all the files required
# 4. generate the code for the entire project including all the files, test the generated code by running the main file and debug it if required
# 5. Use a simple python script in order to save the code in the current directory do not make use of the terminal to save the file.

# Important instructions:
# 1. chrome driver is present in the current directory and the path to the chrome driver is as follows : `chromedriver.exe`
# 2. use the xpaths only for accessing the elements on the webpage
# 3. use the json file with the name `amazon.json` in the current directory for getting the xpaths of the required elements
          
                 
# package stepdefinitions;
# import implementation.Implementation;
# import io.cucumber.java.en.Given;
# import io.cucumber.java.en.When;
# import io.cucumber.java.en.Then;

# public class StepDefinition {{
#     public Implementation implementation = new Implementation();

#     @Given("the user is on the home page")
#     public void launchUrl(){{
#         implementation.launchUrl(url);
#     }}

#     @When("the user clicks on login button")
#         public void userClicksOnLoginButton() {{
#             implementation.clickOnLoginButton();
#     }}

#     @Then("username and password fields should appear")
#         public void verifyLoginWindowAppears() {{
#             implementation.verifyLoginElements();
#     }}

#     @Then("close the browser")
#     public void closeBrowser(){{
#         implementation.closeBrowser();
#     }}
# }}

# Important points:
# 1. The above code is just an example.
# 2. Ensure the step definition file contains launchUrl and closeBrowser methods.
#     @Given("the user is on the home page")
#     public void launchUrl(){{
#         String url = ""; // give the URL here that you want to launch
#         implementation.launchUrl();
#     }}

#     @Then("close the browser")
#     public void closeBrowser(){{
#         implementation.closeBrowser();
#     }}
# """)


# interpreter.chat("""
# Your task is to run and check the Maven project made in the current directory whose information is the following

# the `src` folder has got the implementation and test files 
# the `pom.xml` has got the dependencies

# You can use the following steps for completing the tasks:
# 1. assume maven is installed and chromedriver is present in the current directory
# 2. if you do not have access to the terminal then run the commands for testing the maven project using python script and debug the java code as per requirement
# 3. debug and change the code if required, at the end the code must be in running correctly                         
# """)
