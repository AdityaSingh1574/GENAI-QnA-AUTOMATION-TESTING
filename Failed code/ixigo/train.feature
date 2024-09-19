Feature: ixigo Flight Booking for Cheapest Options at https://www.ixigo.com/flights
    As a budget-conscious traveler
    I want to search for and book the cheapest flights on ixigo
    So that I can travel within my budget constraints

Scenario: Search and Select the cheapest flight with valid city names and dates
    Given the user is on the flight search page
    When the user enters "New Delhi" into the "From" field
    And the user selects "New Delhi" from the dropdown
    And the user enters "Mumbai" into the "To" field
    And the user selects "Mumbai" from the dropdown
    And the user clicks on "Departure" field
    And the user clicks on "Exact Date" button to be selected as "10-10-2024"
    And the user clicks on the search button
    Then a list of available flights from New Delhi to Mumbai on "2024-10-10" is displayed
    When the user clicks on "Price Low to High" button
    And the user clicks on first flight "Book" button
    Then the booking confirmation page for the selected cheapest flight is displayed
