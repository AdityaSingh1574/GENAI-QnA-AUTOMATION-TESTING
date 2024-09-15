
package stepdefinitions;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.junit.Assert;

public class AmazonDropdownStepDefinitions {
    private WebDriver driver;
    private WebDriverWait wait;

    @Given("user is on the Amazon homepage")
    public void userIsOnTheAmazonHomepage() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, 10);
        driver.get("https://www.amazon.com");
    }

    @When("user clicks on the dropdown menu")
    public void userClicksOnTheDropdownMenu() {
        WebElement dropdown = wait.until(ExpectedConditions.elementToBeClickable(By.id("searchDropdownBox")));
        dropdown.click();
    }

    @When("user selects {string} from the dropdown")
    public void userSelectsFromTheDropdown(String option) {
        WebElement optionElement = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//option[text()='" + option + "']")));
        optionElement.click();
    }

    @Then("{string} should be displayed as the selected option")
    public void shouldBeDisplayedAsTheSelectedOption(String expectedOption) {
        WebElement selectedOption = driver.findElement(By.xpath("//select[@id='searchDropdownBox']/option[@selected='selected']"));
        Assert.assertEquals(expectedOption, selectedOption.getText());
        driver.quit();
    }
}
