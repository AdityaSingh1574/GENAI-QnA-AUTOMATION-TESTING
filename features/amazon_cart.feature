
Feature: Add Items to Cart on Amazon.in
  As a user, I want to search for various items on Amazon and add them to my cart

  Scenario: Search and Add Book to Cart
    Given the user is on the Amazon.in homepage
    When the user searches for "Book" in the search box
    And the user selects the first "Book" from the search results
    And the user clicks on "Add to Cart" button
    Then the "Book" should be added to the user's cart
    And the cart count should increase by 1

  Scenario: Search and Add Shoes to Cart
    Given the user is on the Amazon.in homepage
    When the user searches for "Shoes" in the search box
    And the user selects the first "Shoes" from the search results
    And the user selects the desired size and color
    And the user clicks on "Add to Cart" button
    Then the "Shoes" should be added to the user's cart
    And the cart count should increase by 1
