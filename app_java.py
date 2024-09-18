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



# locator file
# interpreter.chat("""
# The following is a JSON between `---XPATH-START---` and `---XPATH-END---` which contains Xpaths for elements in a website
# ---XPATH-START---
# {
#     "langauge_change_button" : "//*[@id="icp-nav-flyout"]",
#     "english_checkbox" : "//*[@id="icp-language-settings"]/div[2]/div/label/i",
#     "hindi_checkbox" : "//*[@id="icp-language-settings"]/div[3]/div/label/i",
#     "save_changes" : "//*[@id="icp-save-button"]/span/input"
# }
# ---XPATH-END---

# Your task is to generate a `Locator.java` file and save it to the current directory
# An Example of the locator file is as follows:

# package locators;
# public class Locators {{
#     public static By loginButton = By.xpath("//span[text()='Login with Gemini mail!']");
#     public static By firstName = By.xpath("//input[contains(@class,'first-name')]");
#     public static String textField = "//input[@id='email']";
# }}

# Important instructions:
# 1. Add necessary import statements. 

# When the Locators file is created save it the current directory using a python script
# """)
                

interpreter.chat("""
---FEATURE-FILE-START---

Feature: Add Books in the cart from Amazon on https://www.amazon.in/
As a user, I want to select my preferred language on Amazon

Scenario: Select English as the preferred language
Given user opens Amazon homepage
When user clicks on the "Change Language" button
And a page opens for changing the language
And user selects "English" from the language options
And user clicks on the "Save Changes" button

Scenario: Select Hindi as the preferred language
Given user opens Amazon homepage
When user clicks on the "Change Language" button
And a page opens for changing the language
And user selects "Hindi" from the language options
And user clicks on the "Save Changes" button
    
---FEATURE-FILE-END---

the feature file is given between `---FEATURE-FILE-START---` and `---FEATURE-FILE-END---`
Your task will be to implement the step definition file using the above given feature file text in JAVA

You can use the following instructions for generating step definition and implementation files
1. Go through and understand the text of the feature file to comprehend the steps that need to be implemented.
2. Step definition file will contain the Python code that defines the steps for the feature file text 
3. the implementation file will contain the actual implementation of the test case / feature file containing the imports from step definition file.
4. Divide feature file big task into small steps / tasks and implement the functions for getting the steps done
5. Implement all the functions in the implementation and step definition files for completing the task
5. When done save the file in the current directory using a simple  python script

use the following as locators as Xpaths for implementing the step definition file for accessing the element 
The Xpaths are given between `---XPATH-START---` and `---XPATH-END---`

---XPATH-START---
{
    "langauge_changer_link" : "//*[@id="icp-nav-flyout"]",
    "english_checkbox" : "//*[@id="icp-language-settings"]/div[2]/div/label/i",
    "hindi_checkbox" : "//*[@id="icp-language-settings"]/div[3]/div/label/i",
    "save_changes" : "//*[@id="icp-save-button"]/span/input"
}
---XPATH-END---


The following can be used as an example for a step definition file
package stepdefinitions;
import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class StepDefinition {{
    public Implementation implementation = new Implementation();

    @Given("the user is on the home page")
    public void launchUrl(){{
        implementation.launchUrl(url);
    }}

    @When("the user clicks on login button")
        public void userClicksOnLoginButton() {{
            implementation.clickOnLoginButton();
    }}

    @Then("username and password fields should appear")
        public void verifyLoginWindowAppears() {{
            implementation.verifyLoginElements();
    }}

    @Then("close the browser")
    public void closeBrowser(){{
        implementation.closeBrowser();
    }}
}}

Important instructions:
1. Save the code for the implementation and step definition files using a simple python script, do not use terminal for writing in files.
2. The Xpaths given are accurate hence do not generate on your own
3. Do not use chromedriver.exe for accessing the browser instead use WebDriverManager library for the same. 
4. Ensure the step definition file contains launchUrl and closeBrowser methods.
    @Given("the user is on the home page")
    public void launchUrl(){{
        String url = ""; // give the URL here that you want to launch
        implementation.launchUrl();
    }}

    @Then("close the browser")
    public void closeBrowser(){{
        implementation.closeBrowser();
    }}

""")




# interpreter.chat("""
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



# follow the instructions in order to complete the task:
# 1. Go through the feature file above and identify the names of the elements on which the actions are to be performed, to implement the locator file
# 2. Identify the steps that are to be done for the task to get completed, using this implement the step definition file
# 3. divide single task into sub tasks and generate the functions for completing the steps and hence generate the implementation file


# use the following JSON for getting the xpaths of the required elements

# {
#     "search_bar" : "//*[@id="twotabsearchtextbox"]",
#     "search_button" : "//*[@id="nav-search-submit-button"]",
#     "first_search_result" : "//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span",
#     "add_to_cart" : "//*[@id="add-to-cart-button"]",
#     "cart_counter" : "//*[@id="nav-cart-count"]"
# }


# Important instructions:
# 1. chrome driver is present in the current directory and the path to the chrome driver is as follows : `chromedriver.exe`
# 2. use the xpaths only for accessing the elements on the webpage
# 3. implement all the steps in all the files, do not leave for the user to implement it


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
