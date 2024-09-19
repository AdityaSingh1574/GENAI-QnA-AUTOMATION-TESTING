package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("the user is on the flight search page")
    public void launchUrl() {
        String url = "https://www.ixigo.com/flights";
        implementation.launchUrl(url);
    }

    @When("the user enters {string} into the {string} field")
    public void enterCityName(String cityName, String fieldName) {
        implementation.enterCityName(cityName, fieldName);
    }

    @When("the user selects {string} from the dropdown")
    public void selectCityFromDropdown(String cityName) {
        implementation.selectCityFromDropdown(cityName);
    }

    @When("the user clicks on {string} field")
    public void clickOnField(String fieldName) {
        implementation.clickOnField(fieldName);
    }

    @When("the user clicks on {string} button to be selected as {string}")
    public void selectExactDate(String buttonName, String date) {
        implementation.selectExactDate(buttonName, date);
    }

    @When("the user clicks on the search button")
    public void clickSearchButton() {
        implementation.clickSearchButton();
    }

    @Then("a list of available flights from New Delhi to Mumbai on {string} is displayed")
    public void verifyFlightListDisplayed(String date) {
        implementation.verifyFlightListDisplayed(date);
    }

    @When("the user clicks on {string} button")
    public void clickOnButton(String buttonName) {
        implementation.clickOnButton(buttonName);
    }

    @When("the user clicks on first flight {string} button")
    public void clickOnFirstFlightBookButton(String buttonName) {
        implementation.clickOnFirstFlightBookButton(buttonName);
    }

    @Then("the booking confirmation page for the selected cheapest flight is displayed")
    public void verifyBookingConfirmationPage() {
        implementation.verifyBookingConfirmationPage();
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}