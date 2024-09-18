
package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.And;

public class StepDefinition {
    public Implementation implementation = new Implementation();

    @Given("user opens Amazon homepage")
    public void launchUrl() {
        String url = "https://www.amazon.in/";
        implementation.launchUrl(url);
    }

    @When("user clicks on the {string} button")
    public void clickChangeLanguageButton(String buttonName) {
        implementation.clickChangeLanguageButton();
    }

    @And("a page opens for changing the language")
    public void verifyLanguageChangePage() {
        implementation.verifyLanguageChangePage();
    }

    @And("user selects {string} from the language options")
    public void selectLanguage(String language) {
        implementation.selectLanguage(language);
    }

    @And("user clicks on the {string} button")
    public void clickSaveChangesButton(String buttonName) {
        implementation.clickSaveChangesButton();
    }

    @And("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
