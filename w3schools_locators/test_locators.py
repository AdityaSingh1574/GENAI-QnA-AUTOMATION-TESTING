
import json
import requests
from bs4 import BeautifulSoup

def test_locators():
    # Load locators from JSON file
    with open('w3schools_tryit_locators.json', 'r') as f:
        locators = json.load(f)

    # Fetch the page content
    url = "https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_form_steps"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Test each locator
    for name, locator in locators.items():
        try:
            if locator['type'] == 'id':
                element = soup.find(id=locator['value'])
            elif locator['type'] == 'class':
                element = soup.find(class_=locator['value'])
            elif locator['type'] == 'name':
                element = soup.find(attrs={"name": locator['value']})
            
            if element:
                print(f"Locator '{name}' found successfully")
                print(f"  Tag: {element.name}")
                print(f"  Attributes: {element.attrs}")
            else:
                print(f"Error: Locator '{name}' not found")
        except Exception as e:
            print(f"Error: Locator '{name}' caused an exception. Error: {str(e)}")

    # Print out the overall structure of the page
    print("Page Structure:")
    for element in soup.find_all(recursive=False):
        print(f"- {element.name}: {element.get('id', '')} {element.get('class', '')}")

if __name__ == "__main__":
    test_locators()
