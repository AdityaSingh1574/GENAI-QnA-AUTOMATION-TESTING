package stepdefinitions;

import implementation.Implementation;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.And;

public class AmazonCartStepDefinition {
    private Implementation implementation = new Implementation();
    private int initialCartCount;

    @Given("user is on the Amazon homepage")
    public void launchUrl() {
        String url = "https://www.amazon.in";
        implementation.launchUrl(url);
    }

    @When("user searches for {string} in the search box")
    public void searchForItem(String item) {
        implementation.searchForItem(item);
    }

    @And("user selects the first {string} from the search results")
    public void selectFirstItem(String item) {
        implementation.selectFirstItem();
    }

    @And("user clicks on 'Add to Cart' button")
    public void clickAddToCart() {
        initialCartCount = implementation.getCartCount();
        implementation.clickAddToCart();
    }

    @Then("the {string} should be added to the user's cart")
    public void verifyItemAddedToCart(String item) {
        implementation.verifyItemAddedToCart(item);
    }

    @And("the cart count should increase by 1")
    public void verifyCartCountIncrease() {
        int newCartCount = implementation.getCartCount();
        assert newCartCount == initialCartCount + 1 : "Cart count did not increase by 1";
    }

    @Then("close the browser")
    public void closeBrowser() {
        implementation.closeBrowser();
    }
}