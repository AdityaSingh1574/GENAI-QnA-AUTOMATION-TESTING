from interpreter import interpreter
# import vertexai
from dotenv import load_dotenv
import os
load_dotenv()


# vertexai.init(project="open-interpreter-testing")

# interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.auto_run = True
interpreter.llm.model = "openai/claude-3-5-sonnet"
interpreter.llm.api_base = 'http://localhost:4000'
interpreter.llm.supports_vision = True
interpreter.llm.supports_functions = True
interpreter.llm.temperature = 0.1

# interpreter.llm.api_key = os.getenv("OPENAI_API_KEY") 
# interpreter.auto_run = True
# interpreter.llm.model = "openai/gpt-4o-mini"
# interpreter.llm.temperature = 0.1


# interpreter.system_message="""
# You are a helpful assistant
# You will be instructed to visit a website using a given URL and some instructions in gherkin syntax
# You have to generate the code for completing the tasks present in the user message
# """

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

# interpreter.chat("Visit https://www.myntra.com and extract the feature name and their descriptions and save them in a txt file in the current directory")


interpreter.chat("""
Feature: Select Options from Dropdown on Amazon Homepage
  As a user, I want to select different options from the dropdown menu on Amazon's homepage

  Scenario: Select All Categories from Dropdown
    Given user is on the Amazon homepage
    When user clicks on the dropdown menu
    And user selects "All Categories" from the dropdown
    Then "All Categories" should be displayed as the selected option

  Scenario: Select Alexa Skills from Dropdown
    Given user is on the Amazon homepage
    When user clicks on the dropdown menu
    And user selects "Alexa Skills" from the dropdown
    Then "Alexa Skills" should be displayed as the selected option

follow the instructions in order to complete the task:
1. Given a  feature file, generate a working step definition file in Java that maps all steps in the feature file to corresponding methods in the step definition file.
2. If an error is encountered then analyse the error, traceback the source of the error and fix the error 
3. Save the code in the current directory

Important instructions
1. First, make sure you have a Maven or Gradle project set up with the following dependencies:
    • Cucumber Java
    • Cucumber JUnit
    • Selenium Java
    • JUnit
2. complete the initial setup by creating a pom.xml and other requirements, assume everything needs to be installed an d a project must be created
3. Use a simple python script in order to save the code in the current directory do not make use of the terminal to save the file.
4. Run the files in the environment you have created and debug them if they do not work, To run the tests, you would typically use Maven. Get access to it if you dont have it.


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

Important points:
1. The above code is just an example.
3. Ensure the step definition file contains launchUrl and closeBrowser methods.
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

# interpreter.chat("use the filepath : C:\\Users\\aditya.singh1\\Desktop\\GEN-AI-AUTO\\GENAI-QnA-AUTOMATION-TESTING\\input_images\\flipkart_lading_page.png and show the image using code, save the code once done")
# LEVEL 01 EXAMPLES
# interpreter.chat("Visit https://www.flipkart.com and scroll down by 500 pixels to reach the trending section. Take a screenshot of the trending items and save it.Save the Code")
# interpreter.chat("Go to https://www.snapdeal.com and click on 'Sports Footwear' section. Take a screenshot of this section and save it.Save the Code")
# interpreter.chat("Navigate to https://www.myntra.com and hover over the 'Men' section on the homepage. Take a screenshot of the dropdown menu that appears and save it.Save the Code")
# interpreter.chat("Visit https://www.amazon.in and click on 'Amazon miniTV'. Refresh the page three times and take a screenshot of the third refresh state.Save the Code")
# interpreter.chat("Access https://www.tatacliq.com and Hover over 'Brands' and click on 'Men's Wear' on the menu which appears after hovering. Take a screenshot capturing the displayed products and save it.Save the Code") # failed
# interpreter.chat("Go to https://www.ajio.com and zoom in by 150 percent on the homepage. Take a screenshot of the zoomed-in view.Save the Code")
# interpreter.chat("Visit https://www.croma.com and scroll to the footer of the homepage and type in the email 'ariesatgemini@gmail.com' in 'CONNECT WITH US' and click on the arrow. Take a screenshot that captures the contact information and save it.Save the Code")
# interpreter.chat("Navigate to https://www.reliancedigital.in and refresh the homepage five times to ensure stability of featured content. Take a screenshot of the homepage after the last refresh.Save the Code")
# interpreter.chat("Visit https://www.shopclues.com and find the 'Flash Deals' section without scrolling. Take a screenshot of this section and save it.Save the Code")
# interpreter.chat("Go to https://www.jiomart.com and hover over the 'Groceries' section to display its submenu. Take a screenshot of the submenu and save it.Save the Code")
# interpreter.chat("Navigate to https://www.bigbasket.com and scroll down to the 'Best Sellers' section on the homepage. Take a screenshot and save it.Save the Code")
# interpreter.chat("Visit https://www.swiggy.com and capture the top navigation bar by taking a screenshot without any scrolling, focusing on the logo and menu items.Save the Code")
# interpreter.chat("Go to https://www.zomato.com and refresh the homepage twice, then take a screenshot of the 'Collections' section that showcases popular eateries.Save the Code")
# interpreter.chat("Access https://www.bookmyshow.com and take a screenshot of the 'Currently Trending Events' section by scrolling down to this specific area.Save the Code")
# interpreter.chat("Navigate to https://www.oyorooms.com and take a screenshot of the 'Top Rated Hotels' section by scrolling down directly to that part of the homepage.Save the Code")
# interpreter.chat("Visit https://www.lenskart.com and hover over the 'Eyeglasses' menu item to reveal the dropdown. Take a screenshot of the expanded dropdown menu.Save the Code")
# interpreter.chat("Go to https://www.nykaa.com and scroll down to the 'New Launches' section on the homepage. Take a screenshot of the new product offerings.Save the Code")
# interpreter.chat("Navigate to https://www.pepperfry.com and take a screenshot of the homepage's main banner which rotates between different promotional offers.Save the Code")
# interpreter.chat("Visit https://www.fabindia.com and focus on the 'Season's Special' section by scrolling down. Take a screenshot of this section and save it.Save the Code")
# interpreter.chat("Access https://www.decathlon.in and find the 'Sports Accessories' section by scrolling, then take a screenshot to capture the featured products.Save the Code")


# LEVEL 2 TEST CASES

# interpreter.chat("Visit https://shop.vaidyaratnammooss.com/arishtas-and-asavaas and click 'ADD TO CART' on any product. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://groww.in/, Find the Search Bar, and Search 'Motilal'. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://web.whatsapp.com/, wait for 30 seconds for me to Scan QR code, now find 'Any (You)' on search bar, click on the chat under the 'Chats' section and message 'how are you ?' 5 times. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.youtube.com/, Search for HuggingFace, Go to the 5th video and return the title. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.ebay.com, find the search bar, and search for 'vintage watches'. Save the resulting code.")
# interpreter.chat("Visit https://www.zomato.com, search for 'Italian white sauce pasta' in the current location, and click on the first option which appears in the search results, save the address of the first result. Save the code for the same")
# interpreter.chat("Visit https://www.airbnb.co.in/ and search for accommodations in 'New York' for next 2 days from current date, and list the prices and locations of the first 5 results ")
# interpreter.chat("Visit https://www.github.com, search for 'machine learning' repositories, and download the README files of the top 3 results . Save the code in the current directory.")
# interpreter.chat("Visit https://www.weather.com, search for the current weather in 'Tokyo', and take the screen shot of details .")
# interpreter.chat("Go to https://www.starbucks.in/, Search for latte and print the results of first 3 drinks. Save the code")
# interpreter.chat("Navigate to https://www.adidas.com, search for 'soccer cleats', and list the names and prices of the top 5 results. Save the code.")
# interpreter.chat("Visit https://artklim.com, find the search button and search for Rose and save take the screenshot and save it to downloads")
# interpreter.chat("Navigate to https://www.overstock.com, search for 'office chairs', and list the colors and prices of the first 5 results . Save the script.")
# interpreter.chat("Go to https://www.ikea.com/in/en/, search for 'bedroom sets', and automate the process of adding the most popular set to the shopping cart . Save the code.")
# interpreter.chat("Visit https://www.vogue.com/search, search for 'summer fashion trends', and scrape the titles of the first 5 articles and save it in a txt file. save the script in the current directory.")
# interpreter.chat("Navigate to https://www.underarmour.in, search for 'workout gear', and list the names, prices, and sizes available for the top 3 results. save the code.")
# interpreter.chat("Visit https://www.pedigree.in/, search for 'dog food', and compare the price  of the first 5 brands listed and take the screenshot for the cheapest . Save the code.")
# interpreter.chat("Visit https://forever21.abfrl.in/, search for 'men’s jackets', and add the cheapest jacket to your cart . Save the code.")
# interpreter.chat("Go to https://www.lg.com/, search for 'refrigerators', and list the energy ratings and prices of the first 5 results . and save the code.")
# interpreter.chat("Visit https://in.indeed.com, search for 'software developer' jobs in 'Gurugram', and save results for first 3 listing in a txt file. Save the script.")



# LEVEL 3 TEST CASES
# interpreter.chat("Visit https://www.flipkart.com, search for 'Apple iPhones', select the iPhone 13, add it to the cart, proceed to the cart, and take a screenshot. Save the code.")
# interpreter.chat("Navigate to https://www.amazon.in, search for 'Samsung Galaxy', click on the first search result, add the item to your wishlist, go to your wishlist, and take a screenshot. Save the code.")
# interpreter.chat("Access https://www.tatacliq.com, search for '4K televisions', select the third item from the list, add it to your cart, go to the checkout page, and take a screenshot. Save the code.")
# interpreter.chat("Visit https://www.ajio.com, find 'Casual Shoes', select a shoe from 'Puma', add to cart, then go to cart, and capture a screenshot of the cart details. Save the code.")
# interpreter.chat("Navigate to https://www.zomato.com, search for 'Italian restaurants in Mumbai', select the third result, place an order for a pizza, proceed to checkout, and take a screenshot of the order summary. Save the code.")
# interpreter.chat("Go to https://www.swiggy.com, search for 'Burger King',click on the  first search result,  Add a 'Crispy Veg Burger', proceed to View cart, and take a screenshot of the checkout page. Save the code.")
# interpreter.chat("Visit https://www.snapdeal.com, search for 'LED bulbs', click on the fifth item, view details, add to cart, proceed to payment options, and take a screenshot of the payment page. Save the code.")
# interpreter.chat("Access https://www.ebay.in, search for 'vintage wrist watches', select the top result, bid on the item, confirm the bid on the next page, and take a screenshot of the bid confirmation. Save the code.")
# interpreter.chat("Navigate to https://www.bookmyshow.com, select a city, choose 'Movies', book tickets for the latest release, select seats, proceed to payment, and take a screenshot of the seat selection. Save the code.")
# interpreter.chat("Go to https://www.nykaa.com, search for 'face masks', select a product from 'L'Oreal', add to bag, go to bag, proceed to checkout, and take a screenshot of the checkout details. Save the code.")
# interpreter.chat("Visit https://www.reliancedigital.in, search for 'laptops', click on a Dell laptop, add to cart, visit the cart, proceed to place the order, and take a screenshot of the order preview. Save the code.")
# interpreter.chat("Navigate to https://www.bigbasket.com, search for 'organic fruits', select apples, add to basket, view basket, go to checkout, and take a screenshot of the basket contents. Save the code.")
# interpreter.chat("Access https://www.jiomart.com, search for 'detergent', choose a brand, add a large pack to the cart, proceed to checkout, and take a screenshot of the payment options. Save the code.")
# interpreter.chat("Visit https://www.decathlon.in, search for 'cycling gear', select a helmet, add to cart, view cart, proceed to checkout, and capture a screenshot of the final cart page. Save the code.")
# interpreter.chat("Go to https://www.lenskart.com, search for 'reading glasses', Click on FLexible, select a pair, click on Buy now, and take a screenshot of the Checkout page. Save the code.")
# interpreter.chat("Navigate to https://www.pepperfry.com, select 'office furniture', choose an office chair, click on 'buy now', and take a screenshot of the checkout page. Save the code.")
# interpreter.chat("Visit https://www.fabindia.com, search for 'men's kurtas', click on a kurta, select size and color, add to bag, go to bag, and take a screenshot of the bag's contents. Save the code.")
# interpreter.chat("Access https://www.vistaprint.in, design a custom T-shirt, add to cart, proceed to preview the design, continue to checkout, and take a screenshot of the final design in the cart. Save the code.")
# interpreter.chat("Navigate to https://www.oyo.com, search for rooms in 'Goa', select a property, book a room, proceed to the booking details page, and take a screenshot of the booking confirmation. Save the code.")

# interpreter.chat("Go to https://www.myntra.com, search for 'Adidas men running shoes', click on the second listing, select size, add to bag, view bag, and take a screenshot of the bag contents. Save the code.")
# interpreter.chat(
# """
# Visit https://www.ebay.com/
# Feature: Search Icon Functionality
# 	As a user, I want to interact with the search icon to access search functionality

# Background: The application is open in a web browser

# Scenario: Search icon visibility and scaling
# # 	Verify that the search icon is visible and scales properly across different screen sizes
# 	Given the user is on a page with the search icon
# 	When the user views the page on different screen sizes
# 	Then the search icon should be clearly visible on all screen sizes
# 	And the search icon should maintain its proportions and quality when scaled

# Scenario: Search icon interaction
# # 	Ensure that clicking the search icon activates the search functionality
# 	Given the user is on a page with the search icon
# 	When the user clicks on the search icon
# 	Then a search input field should appear or become active
# 	And the user should be able to enter search terms in the input field

# Scenario: Search icon accessibility
# # 	Verify that the search icon is accessible to users with assistive technologies
# 	Given the user is using a screen reader
# 	When the user navigates to the search icon
# 	Then the screen reader should announce it as a search function
# 	And the user should be able to activate the search

# """
# )