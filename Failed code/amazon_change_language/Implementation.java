
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

    public void clickChangeLanguageButton() {
        WebElement languageChanger = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"icp-nav-flyout\"]")));
        languageChanger.click();
    }

    public void verifyLanguageChangePage() {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"icp-language-settings\"]")));
    }

    public void selectLanguage(String language) {
        String xpath = language.equalsIgnoreCase("English") ?
                "//*[@id=\"icp-language-settings\"]/div[2]/div/label/i" :
                "//*[@id=\"icp-language-settings\"]/div[3]/div/label/i";
        WebElement languageCheckbox = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(xpath)));
        languageCheckbox.click();
    }

    public void clickSaveChangesButton() {
        WebElement saveChangesButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"icp-save-button\"]/span/input")));
        saveChangesButton.click();
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
