
package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("user is on the Amazon homepage")
    public void launchUrl() {
        String url = "https://www.amazon.in";
        implementation.launchUrl(url);
    }

    @When("user clicks on the dropdown menu")
    public void clickOnDropdownMenu() {
        implementation.clickOnDropdownMenu();
    }

    @When("user selects {string} from the dropdown")
    public void selectOptionFromDropdown(String option) {
        implementation.selectOptionFromDropdown(option);
    }

    @Then("{string} should be displayed as the selected option")
    public void verifySelectedOption(String expectedOption) {
        implementation.verifySelectedOption(expectedOption);
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
