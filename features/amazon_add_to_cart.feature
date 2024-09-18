
Feature: Add item to Amazon cart

  Scenario: User adds a shoe to their cart
    Given user is on Amazon homepage
    When user searches for "running shoes"
    And user selects the first "running shoes" from the search results
    And user selects the desired size and color
    And user clicks on 'Add to Cart' button
    Then the "running shoes" should be added to the user's cart
    And the cart count should increase by 1
