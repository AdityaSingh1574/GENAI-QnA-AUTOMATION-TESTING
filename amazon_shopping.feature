{
  "Feature": "Amazon Shopping Experience",
  "Description": "This feature allows users to search for products, add them to the cart, and navigate through the Amazon website.",
  "Scenarios": [
    {
      "Scenario": "Search and Add to Cart",
      "Steps": [
        {
          "StepType": "Given",
          "Description": "user is on the Amazon homepage"
        },
        {
          "StepType": "When",
          "Description": "user searches for \"Book\" in the search box"
        },
        {
          "StepType": "And",
          "Description": "user clicks on the first search result"
        },
        {
          "StepType": "And",
          "Description": "user clicks on the \"Add to Cart\" button"
        },
        {
          "StepType": "Then",
          "Description": "the item should be added to the cart"
        }
      ]
    },
    {
      "Scenario": "List Search Results",
      "Steps": [
        {
          "StepType": "Given",
          "Description": "user is on the Amazon homepage"
        },
        {
          "StepType": "When",
          "Description": "user searches for \"Shoes\" in the search box"
        },
        {
          "StepType": "Then",
          "Description": "user should see a list of shoe products"
        },
        {
          "StepType": "And",
          "Description": "user should be able to print the names of the listed products"
        }
      ]
    },
    {
      "Scenario": "Scroll Page",
      "Steps": [
        {
          "StepType": "Given",
          "Description": "user is on the Amazon homepage"
        },
        {
          "StepType": "When",
          "Description": "user scrolls down to the end of the page"
        },
        {
          "StepType": "Then",
          "Description": "user should see the footer of the page"
        },
        {
          "StepType": "When",
          "Description": "user scrolls back to the top of the page"
        },
        {
          "StepType": "Then",
          "Description": "user should see the Amazon logo and search bar"
        }
      ]
    },
    {
      "Scenario": "Select Category from Dropdown",
      "Steps": [
        {
          "StepType": "Given",
          "Description": "user is on the Amazon homepage"
        },
        {
          "StepType": "When",
          "Description": "user clicks on the category dropdown"
        },
        {
          "StepType": "And",
          "Description": "user selects \"Books\" from the dropdown"
        },
        {
          "StepType": "And",
          "Description": "user performs a search"
        },
        {
          "StepType": "Then",
          "Description": "user should see search results filtered for books"
        }
      ]
    },
    {
      "Scenario": "Change Language",
      "Steps": [
        {
          "StepType": "Given",
          "Description": "user is on the Amazon homepage"
        },
        {
          "StepType": "When",
          "Description": "user clicks on the language selection option"
        },
        {
          "StepType": "And",
          "Description": "user selects \"Hindi\" as the preferred language"
        },
        {
          "StepType": "Then",
          "Description": "the website should be displayed in Hindi"
        }
      ]
    }
  ]
}