
package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("the user is on the AccuWeather search page")
    public void launchUrl() {
        String url = "https://www.accuweather.com/";
        implementation.launchUrl(url);
    }

    @When("the user types {string} into the location input field and presses enter")
    public void typeLocationAndPressEnter(String location) {
        implementation.typeLocationAndPressEnter(location);
    }

    @When("the user is redirected to a new page displaying search results")
    public void verifySearchResultsPage() {
        implementation.verifySearchResultsPage();
    }

    @When("the user selects the first option from the search results")
    public void selectFirstSearchResult() {
        implementation.selectFirstSearchResult();
    }

    @When("the user is redirected to a new page detailing the location")
    public void verifyLocationDetailsPage() {
        implementation.verifyLocationDetailsPage();
    }

    @When("the user clicks on {string}")
    public void clickOnCurrentWeather(String linkText) {
        implementation.clickOnCurrentWeather(linkText);
    }

    @Then("the user is redirected to a page displaying the current weather information for {string}")
    public void verifyCurrentWeatherPage(String location) {
        implementation.verifyCurrentWeatherPage(location);
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
