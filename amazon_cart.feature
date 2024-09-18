
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
