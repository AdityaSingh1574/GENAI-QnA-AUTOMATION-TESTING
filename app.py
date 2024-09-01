from interpreter import interpreter
# import vertexai
from dotenv import load_dotenv
import os
load_dotenv()


# vertexai.init(project="open-interpreter-testing")

# interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.auto_run = True
interpreter.llm.model = "openai/gpt-4o-mini"
interpreter.llm.api_base = 'http://localhost:4000'
interpreter.llm.supports_vision = True
interpreter.llm.supports_functions = True
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



# LEVEL 01 EXAMPLES
interpreter.chat("Visit https://www.flipkart.com and scroll down by 500 pixels to reach the trending section. Take a screenshot of the trending items and save it.Save the Code")
interpreter.chat("Go to https://www.snapdeal.com and scroll down to access the 'Deals of the Day' section. Take a screenshot of this section and save it.Save the Code")
interpreter.chat("Navigate to https://www.myntra.com and hover over the 'Men' section on the homepage. Take a screenshot of the dropdown menu that appears and save it.Save the Code")
interpreter.chat("Visit https://www.amazon.in and scroll to the 'Amazon Prime' advertisement section. Refresh the page three times and take a screenshot of the third refresh state.Save the Code")
interpreter.chat("Access https://www.tatacliq.com and scroll down to the 'New Arrivals' section. Take a screenshot capturing the displayed products and save it.Save the Code")
interpreter.chat("Go to https://www.ajio.com and zoom in by 150 percent on the homepage to enhance the visibility of 'Featured Brands'. Take a screenshot of the zoomed-in view.Save the Code")
interpreter.chat("Visit https://www.croma.com and scroll to the footer of the homepage. Take a screenshot that captures the contact information and save it.Save the Code")
interpreter.chat("Navigate to https://www.reliancedigital.in and refresh the homepage five times to ensure stability of featured content. Take a screenshot of the homepage after the last refresh.Save the Code")
interpreter.chat("Visit https://www.shopclues.com and find the 'Flash Deals' section without scrolling. Take a screenshot of this section and save it.Save the Code")
interpreter.chat("Go to https://www.jiomart.com and hover over the 'Groceries' section to display its submenu. Take a screenshot of the submenu and save it.Save the Code")
interpreter.chat("Navigate to https://www.bigbasket.com and scroll down to the 'Best Sellers' section on the homepage. Take a screenshot and save it.Save the Code")
interpreter.chat("Visit https://www.swiggy.com and capture the top navigation bar by taking a screenshot without any scrolling, focusing on the logo and menu items.Save the Code")
interpreter.chat("Go to https://www.zomato.com and refresh the homepage twice, then take a screenshot of the 'Collections' section that showcases popular eateries.Save the Code")
interpreter.chat("Access https://www.bookmyshow.com and take a screenshot of the 'Currently Trending Events' section by scrolling down to this specific area.Save the Code")
interpreter.chat("Navigate to https://www.oyorooms.com and take a screenshot of the 'Top Rated Hotels' section by scrolling down directly to that part of the homepage.Save the Code")
interpreter.chat("Visit https://www.lenskart.com and hover over the 'Eyeglasses' menu item to reveal the dropdown. Take a screenshot of the expanded dropdown menu.Save the Code")
interpreter.chat("Go to https://www.nykaa.com and scroll down to the 'New Launches' section on the homepage. Take a screenshot of the new product offerings.Save the Code")
interpreter.chat("Navigate to https://www.pepperfry.com and take a screenshot of the homepage's main banner which rotates between different promotional offers.Save the Code")
interpreter.chat("Visit https://www.fabindia.com and focus on the 'Season's Special' section by scrolling down. Take a screenshot of this section and save it.Save the Code")
interpreter.chat("Access https://www.decathlon.in and find the 'Sports Accessories' section by scrolling, then take a screenshot to capture the featured products.Save the Code")


# LEVEL 2 TEST CASES

# interpreter.chat("Visit https://shop.vaidyaratnammooss.com/arishtas-and-asavaas and click 'ADD TO CART' on any product. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://groww.in/, Find the Search Bar, and Search 'Motilal'. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://web.whatsapp.com/, Click on Link with Phone Number, wait for 30 seconds for me to Scan QR code, now find 'Any (You)' on search bar, click on the chat and message 'how are you ?' 5 times. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.youtube.com/, Search for HuggingFace, Go to the 5th video and return the title. Finally Save the working code in the current directory")
# interpreter.chat("Visit https://www.amazon.in, search for 'wireless headphones', and add the first product to your cart. and. Save the code in the current directory")
# interpreter.chat("Visit https://www.ebay.com, find the search bar, and search for 'vintage watches'. Save the resulting code.")
# interpreter.chat("Visit https://www.zomato.com, search for 'Italian restaurants' in your area, and capture the names and ratings of the first 10 results ..")
# interpreter.chat("Visit https://www.airbnb.com, search for accommodations in 'New York' for any date, and list the prices and locations of the first 5 results ")
# interpreter.chat("Visit https://www.github.com, search for 'machine learning' repositories, and download the README files of the top 3 results . Save the code in the current directory.")
# interpreter.chat("Visit https://www.weather.com, search for the current weather in 'Tokyo', and take the screen shot of details .")
# interpreter.chat("Go to https://www.starbucks.in/, Search for latte and print the results of first 3 drinks. Save the code")
# interpreter.chat("Navigate to https://www.adidas.com, search for 'soccer cleats', and list the names and prices of the top 5 results. Save the code.")
# interpreter.chat("Visit https://artklim.com, find the search button and search for Rose and save take the screenshot and save it to downloads ")
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
# interpreter.chat("Go to https://www.myntra.com, search for 'Adidas men running shoes', click on the second listing, select size, add to bag, view bag, and take a screenshot of the bag contents. Save the code.")
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
