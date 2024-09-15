Feature: Add Books in the cart from Amazon on https://www.amazon.in/
  As a user, I want to select my preferred language on Amazon
 
  Scenario: Select English as the preferred language
    Given user opens the language tab on Amazon homepage
    When user selects "English" from the language options
    Then the website should display in English language
    And user preferences should be updated to English
 
  Scenario: Select Hindi as the preferred language
    Given user opens the language tab on Amazon homepage
    When user selects "Hindi" from the language options
    Then the website should display in Hindi language
    And user preferences should be updated to Hindi