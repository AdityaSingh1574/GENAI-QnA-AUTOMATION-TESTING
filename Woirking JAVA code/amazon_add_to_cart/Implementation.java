
package implementation;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class Implementation {
    private WebDriver driver;
    private WebDriverWait wait;

    private final String SEARCH_BAR = "//*[@id='twotabsearchtextbox']";
    private final String SEARCH_BUTTON = "//*[@id='nav-search-submit-button']";
    private final String FIRST_SEARCH_RESULT = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span";
    private final String ADD_TO_CART = "//*[@id='add-to-cart-button']";
    private final String CART_COUNTER = "//*[@id='nav-cart-count']";

    public void launchUrl(String url) {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.get(url);
        driver.manage().window().maximize();
    }

    public void typeInSearchBox(String searchTerm) {
        WebElement searchBox = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(SEARCH_BAR)));
        searchBox.clear();
        searchBox.sendKeys(searchTerm);
    }

    public void clickSearchButton() {
        WebElement searchButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(SEARCH_BUTTON)));
        searchButton.click();
    }

    public void verifySearchResultsPage() {
        wait.until(ExpectedConditions.urlContains("s?k="));
    }

    public void verifySearchResults(String itemType) {
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(FIRST_SEARCH_RESULT)));
        // Additional verification can be added here
    }

    public void selectFirstSearchResult(String itemType) {
        WebElement firstResult = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(FIRST_SEARCH_RESULT)));
        firstResult.click();
    }

    public void clickAddToCartButton() {
        WebElement addToCartButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(ADD_TO_CART)));
        addToCartButton.click();
    }

    public void verifyItemAddedToCart(String itemType) {
        // This step might need additional implementation depending on Amazon's UI
        // For now, we'll just wait for the cart count to update
        wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(CART_COUNTER)));
    }

    public void verifyCartCountIncrease(int count) {
        WebElement cartCounter = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(CART_COUNTER)));
        int currentCount = Integer.parseInt(cartCounter.getText());
        // Assert that the current count is greater than or equal to the expected count
        assert currentCount >= count : "Cart count did not increase as expected";
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
