
package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("the user is on the Groww SIP calculator page on {}")
    public void launchUrl(String url) {
        implementation.launchUrl(url);
    }

    @When("the user enters {string} into the {string} field")
    public void enterValueIntoField(String value, String fieldName) {
        implementation.enterValueIntoField(value, fieldName);
    }

    @Then("the future values such as Investment amount, Est. returns, and Total value of the investment are displayed")
    public void verifyFutureValuesDisplayed() {
        implementation.verifyFutureValuesDisplayed();
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
