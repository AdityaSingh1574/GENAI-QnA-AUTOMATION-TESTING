
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

    public void launchUrl(String url) {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(url);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void enterValueIntoField(String value, String fieldName) {
        String xpath;
        switch (fieldName) {
            case "Monthly investment":
                xpath = "//*[@id=\"MONTHLY_INVESTMENT\"]";
                break;
            case "Time period":
                xpath = "//*[@id=\"TIME_PERIOD\"]";
                break;
            case "Expected return rate (p.a)":
                xpath = "//*[@id=\"RETURN_RATE\"]";
                break;
            default:
                throw new IllegalArgumentException("Invalid field name: " + fieldName);
        }
        WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpath)));
        element.clear();
        element.sendKeys(value);
    }

    public void verifyFutureValuesDisplayed() {
        String[] xpaths = {
            "//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/span/span",
            "//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/span/span",
            "//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[3]/div[2]/span/span"
        };

        for (String xpath : xpaths) {
            WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(xpath)));
            assert element.isDisplayed() : "Future value element is not displayed: " + xpath;
        }
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
