package implementation;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import io.github.bonigarcia.wdm.WebDriverManager;

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

    public void enterCityName(String cityName, String fieldName) {
        String xpath = fieldName.equals("From") ? 
            "/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/input" :
            "/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/input";
        WebElement inputField = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
        inputField.clear();
        inputField.sendKeys(cityName);
    }

    public void selectCityFromDropdown(String cityName) {
        String xpath = cityName.equals("New Delhi") ?
            "/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/li" :
            "/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/li";
        WebElement cityOption = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
        cityOption.click();
    }

    public void clickOnField(String fieldName) {
        if (fieldName.equals("Departure")) {
            WebElement departureField = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/p[2]")));
            departureField.click();
        }
    }

    public void selectExactDate(String buttonName, String date) {
        WebElement exactDateButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[12]")));
        exactDateButton.click();
    }

    public void clickSearchButton() {
        WebElement searchButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/button/svg/path")));
        searchButton.click();
    }

    public void verifyFlightListDisplayed(String date) {
        // Implement verification logic here
    }

    public void clickOnButton(String buttonName) {
        if (buttonName.equals("Price Low to High")) {
            WebElement sortButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/span/span")));
            sortButton.click();
        }
    }

    public void clickOnFirstFlightBookButton(String buttonName) {
        WebElement bookButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/button")));
        bookButton.click();
    }

    public void verifyBookingConfirmationPage() {
        // Implement verification logic here
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}