Feature: MultiSteps Form Automation with Screenshot and Screen Recording
  As a user, I want to fill out a multi-step form on https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_form_steps

  Scenario: User Fills and Completes the Multi-Step Form
    Given user opens the multiStepForm
    When user fills in the "First name" field with 'Aditya'
    And user fills in the "Last name" field with 'Singh'
    And user clicks the "Next" button to proceed to the next step
    And user fills in the "E-mail" field with 'abc@bb.com'
    And user fills in the "Phone" field with '+123456789'
    And user clicks the "Next" button to proceed to the next step
    And user fills in the "dd" field for birth date as '30'
    And user fills in the "mm" field for birth month as '09'
    And user fills in the "yyyy" field for birth year as '2000'
    And user clicks the "Next" button to proceed to the next step
    And user fills in the "Username" field with 'adi1674'
    And user fills in the "Password" field with '123@bbc'
    When user completes all steps of the form
    And user clicks the "Submit" button
    Then the form should be successfully submitted