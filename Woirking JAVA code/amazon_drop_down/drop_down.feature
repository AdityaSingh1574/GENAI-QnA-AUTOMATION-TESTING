Feature: Select Options from Dropdown on Amazon Homepage at https://www.amazon.in
  As a user, I want to select different options from the dropdown menu on Amazon's homepage

  Scenario: Select Amazon Fashion from Dropdown
    Given user is on the Amazon homepage
    When user clicks on the dropdown menu
    And user selects "Amazon Fashion" from the dropdown
    Then "Amazon Fashion" should be displayed as the selected option

  Scenario: Select Alexa Skills from Dropdown
    Given user is on the Amazon homepage
    When user clicks on the dropdown menu
    And user selects "Alexa Skills" from the dropdown
    Then "Alexa Skills" should be displayed as the selected option