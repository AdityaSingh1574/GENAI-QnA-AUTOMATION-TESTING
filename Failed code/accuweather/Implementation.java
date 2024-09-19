
package implementation;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
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
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.get(url);
    }

    public void typeLocationAndPressEnter(String location) {
        WebElement inputLocation = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input")));
        inputLocation.sendKeys(location);
        inputLocation.sendKeys(Keys.ENTER);
    }

    public void verifySearchResultsPage() {
        wait.until(ExpectedConditions.urlContains("search-results"));
    }

    public void selectFirstSearchResult() {
        WebElement firstResult = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div/div[6]/div[1]/div[1]/div[2]/a[1]")));
        firstResult.click();
    }

    public void verifyLocationDetailsPage() {
        wait.until(ExpectedConditions.urlContains("weather-forecast"));
    }

    public void clickOnCurrentWeather(String linkText) {
        WebElement currentWeatherLink = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div/div[7]/div[1]/div[1]/a[1]")));
        currentWeatherLink.click();
    }

    public void verifyCurrentWeatherPage(String location) {
        wait.until(ExpectedConditions.urlContains("current-weather"));
        WebElement pageTitle = wait.until(ExpectedConditions.visibilityOfElementLocated(By.tagName("h1")));
        assert pageTitle.getText().contains(location) : "Current weather page for " + location + " not found";
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
