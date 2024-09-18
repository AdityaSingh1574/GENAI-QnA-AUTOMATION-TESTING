
package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.And;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("user is on the Amazon India homepage")
    public void launchUrl() {
        String url = "https://www.amazon.in/";
        implementation.launchUrl(url);
    }

    @When("user searches for {string} in the search box")
    public void userSearchesForItem(String item) {
        implementation.enterSearchTerm(item);
    }

    @And("user clicks the search button")
    public void userClicksSearchButton() {
        implementation.clickSearchButton();
    }

    @Then("user should see a results page listing {string}")
    public void userSeesResultsPage(String item) {
        implementation.verifyResultsPage(item);
    }

    @And("user prints the names of first 5 {string} results")
    public void userPrintsFirstFiveResults(String item) {
        implementation.printFirstFiveResults(item);
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
