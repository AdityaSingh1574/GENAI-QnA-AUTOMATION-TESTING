from interpreter import interpreter
# import vertexai
from dotenv import load_dotenv
import os
load_dotenv()


# vertexai.init(project="open-interpreter-testing")

# interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.auto_run = True
interpreter.llm.model = "openai/mistral-large-2407"
interpreter.llm.api_base = 'http://localhost:4000'
interpreter.llm.temperature = 0.1

# interpreter.llm.api_key = os.getenv("OPENAI_API_KEY") 
# interpreter.auto_run = True
# interpreter.llm.model = "openai/gpt-4o-mini"
# interpreter.llm.temperature = 0.1


interpreter.custom_instructions = """You need to follow these instructions to execute the given Task:
1. Plan Out your task and divide them into subtasks.
2. If you get xpath error you analyze the the html content and try to find the correct xpath. You can Ignore tags like  <script> , <link>, <iframe>
3. Give an Analysis of why code failed and then proceed with re-writing.
4. To Verify if the Task was successfully done, check which site it has landed to maybe url or title
5. Use Python Selenium and assume chrome driver is already installed.
6. Do not use WebDriverWait function for webdriver to find elements.
7. Save the working code in the current directory after verifying the steps are correct.
"""
 

# interpreter.chat("Visit https://shop.vaidyaratnammooss.com/arishtas-and-asavaas and click 'ADD TO CART' on any product. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://groww.in/, Find the Search Bar, and Search 'Motilal'. and assume chrome driver is already installed. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://web.whatsapp.com/, Click on Link with Phone Number, wait for 30 seconds for me to enter information, now message 'Myself' 'how are you ?' 5 times. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.youtube.com/, Search for HuggingFace, Go to the 5th video and add it to the queue. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.amazon.in, search for 'wireless headphones', and add the first product to your cart. and assume Chrome driver is installed. Save the code in the current directory")
# interpreter.chat("Visit https://www.ebay.com, find the search bar, and search for 'vintage watches'., assuming the Chrome driver is pre-installed. Save the resulting code.")
# interpreter.chat("Visit https://www.zomato.com, search for 'Italian restaurants' in your area, and capture the names and ratings of the first 10 results . Assume Chrome driver is installed.")
# interpreter.chat("Visit https://www.airbnb.com, search for accommodations in 'New York' for next weekend, and list the prices and locations of the first 5 results . Assume Chrome driver installation.")
# interpreter.chat("Visit https://www.github.com, search for 'machine learning' repositories, and download the README files of the top 3 results . Save the code in the current directory.")
# interpreter.chat("Visit https://www.weather.com, search for the current weather in 'Tokyo', and take the screen shot of details . Assume Chrome driver is available.")
# interpreter.chat("Go to https://www.starbucks.in/, Search for latte and print the results of first 3 drinks. Save the code")
# interpreter.chat("Navigate to https://www.adidas.com, search for 'soccer cleats', and list the names and prices of the top 5 results., assuming Chrome driver is ready. Save the code.")
# interpreter.chat("Visit https://www.expedia.com, search for a flight package to 'Las Vegas', and save the first result as text file. Save the code.")
# interpreter.chat("Visit https://artklim.com, find the search button and search for Rose and save take the screenshot and save it to downloads . Assume Chrome driver installation.")
# interpreter.chat("Navigate to https://www.overstock.com, search for 'office chairs', and list the colors and prices of the first 5 results . Save the script.")
# interpreter.chat("Go to https://www.ticketmaster.com, search for 'rock concerts' in 'New York', and list the event dates and prices for the upcoming month . Assume Chrome driver is installed.")

# interpreter.chat("Go to https://www.ikea.com, search for 'bedroom sets', and automate the process of adding the most popular set to the shopping cart . Save the code.")
# interpreter.chat("Visit https://www.vogue.com/search, search for 'summer fashion trends', and scrape the titles of the first 5 articles and save it in a txt file. with Chrome driver pre-installed and save the script in the current directory.")
# interpreter.chat("Navigate to https://www.underarmour.in, search for 'workout gear', and list the names, prices, and sizes available for the top 3 results., assuming Chrome driver is ready, and save the code.")
interpreter.chat("Access https://www.michaels.com, search for 'watercolor paints', and add the top-rated set to your cart., ensuring Chrome driver is installed, and save the code.")
# interpreter.chat("Visit https://www.pedigree.in/, search for 'dog food', and compare the price  of the first 5 brands listed and take the screenshot for the cheapest . Save the code.")
# interpreter.chat("Visit https://forever21.abfrl.in/, search for 'men’s jackets', and add the cheapest jacket to your cart . Save the code.")
# interpreter.chat("Navigate to https://www.priceline.com, search for a round-trip flight from 'Chicago' to 'Miami' and find the total fair. Save the script.")
# interpreter.chat("Go to https://www.lg.com/, search for 'refrigerators', and list the energy ratings and prices of the first 5 results . Assume Chrome driver is installed and save the code.")
# interpreter.chat("Visit https://www.monster.com, search for 'software developer' jobs in 'California', and save results for first 3 listing in a txt file. Save the script.")
# interpreter.chat("Navigate to https://www.saksfifthavenue.com, search for 'designer handbags', and compare the prices of the top 3 choices and save the prices in a csv file with name of the product against price. Save the code.")
