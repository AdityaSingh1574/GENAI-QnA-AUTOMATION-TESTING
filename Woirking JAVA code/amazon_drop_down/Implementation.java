
package implementation;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import static org.junit.Assert.assertEquals;

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

    public void clickOnDropdownMenu() {
        WebElement dropdown = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"nav-search-dropdown-card\"]/div")));
        dropdown.click();
    }

    public void selectOptionFromDropdown(String option) {
        String xpath;
        if (option.equals("Amazon Fashion")) {
            xpath = "//*[@id=\"searchDropdownBox\"]/option[1]";
        } else if (option.equals("Alexa Skills")) {
            xpath = "//*[@id=\"searchDropdownBox\"]/option[2]";
        } else {
            throw new IllegalArgumentException("Invalid option: " + option);
        }

        WebElement optionElement = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
        optionElement.click();
    }

    public void verifySelectedOption(String expectedOption) {
        WebElement selectedOption = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"nav-search-dropdown-card\"]/div/div/span")));
        assertEquals(expectedOption, selectedOption.getText());
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
