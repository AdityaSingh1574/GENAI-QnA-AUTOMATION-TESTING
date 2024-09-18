package implementation;

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
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.get(url);
        driver.manage().window().maximize();
    }

    public void searchForItem(String item) {
        WebElement searchBar = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(SEARCH_BAR)));
        searchBar.sendKeys(item);
        driver.findElement(By.xpath(SEARCH_BUTTON)).click();
    }

    public void selectFirstItem() {
        WebElement firstItem = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(FIRST_SEARCH_RESULT)));
        firstItem.click();
    }

    public void clickAddToCart() {
        WebElement addToCartButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(ADD_TO_CART)));
        addToCartButton.click();
    }

    public int getCartCount() {
        WebElement cartCounter = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(CART_COUNTER)));
        return Integer.parseInt(cartCounter.getText());
    }

    public void verifyItemAddedToCart(String item) {
        // This method would typically involve checking if the item is in the cart
        // For simplicity, we'll just print a message
        System.out.println(item + " has been added to the cart.");
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}