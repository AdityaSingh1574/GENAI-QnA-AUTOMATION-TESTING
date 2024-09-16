
Feature: MultiSteps Form Automation with Screenshot and Screen Recording

Scenario: User Fills and Completes the Multi-Step Form
    Given user opens the multiStepForm
    When user fills in the "First name" field with 'Aditya'
    And user fills in the "Last name" field with 'Singh'
    And user fills in the "E-mail" field with 'abc@bbc.com'
    And user fills in the "Phone" field with '+123456789'
    And user fills in the "dd" field for birth date with '01'
    And user fills in the "mm" field for birth month with '01'
    And user fills in the "yyyy" field for birth year with '2007'
    And user fills in the "Username" field with 'aditya1574'
    And user fills in the "Password" field with '123@bbc'
    And user clicks the "Next" button to proceed to the next step
    Then user should see the next step of the form
    When user completes all steps of the form
    And user clicks the "Submit" button
    Then the form should be successfully submitted
    And a screenshot of the completed form should be captured
    And a screen recording of the form filling process should be saved
