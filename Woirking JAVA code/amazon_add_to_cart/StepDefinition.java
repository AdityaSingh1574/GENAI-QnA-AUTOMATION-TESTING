
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

    @When("user types {string} in the search box")
    public void userTypesInSearchBox(String searchTerm) {
        implementation.typeInSearchBox(searchTerm);
    }

    @When("user clicks on the search button")
    public void userClicksOnSearchButton() {
        implementation.clickSearchButton();
    }

    @Then("user should be redirected to the search results page")
    public void userShouldBeRedirectedToSearchResultsPage() {
        implementation.verifySearchResultsPage();
    }

    @Then("user should see a list of {string} in the search results")
    public void userShouldSeeListOfItemsInSearchResults(String itemType) {
        implementation.verifySearchResults(itemType);
    }

    @When("user selects the first {string} from the search results")
    public void userSelectsFirstItemFromSearchResults(String itemType) {
        implementation.selectFirstSearchResult(itemType);
    }

    @When("user clicks on the 'Add to Cart' button")
    public void userClicksOnAddToCartButton() {
        implementation.clickAddToCartButton();
    }

    @Then("the {string} should be added to the user's cart")
    public void itemShouldBeAddedToCart(String itemType) {
        implementation.verifyItemAddedToCart(itemType);
    }

    @Then("the cart count should increase by {int}")
    public void cartCountShouldIncreaseBy(int count) {
        implementation.verifyCartCountIncrease(count);
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}
