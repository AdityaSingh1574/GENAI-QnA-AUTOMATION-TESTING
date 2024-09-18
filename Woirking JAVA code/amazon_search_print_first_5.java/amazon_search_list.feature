Feature: List Search Options on Amazon India
  As a user, I want to search for various items on Amazon India and list the search results

  Scenario: Search and List Sandals
    Given user is on the Amazon India homepage
    When user searches for 'Sandals' in the search box
    And  user clicks the search button
    Then user should see a results page listing 'Sandals'
    And user prints the names of first 5 'Sandals' results

  Scenario: Search and List Shoes
    Given user is on the Amazon India homepage
    When user searches for 'Shoes' in the search box
    And  user clicks the search button
    Then user should see a results page listing 'Shoes'
    And user prints the names of first 5 'Shoes' results