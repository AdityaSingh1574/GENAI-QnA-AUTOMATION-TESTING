
package implementation;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;

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

    public void enterSearchTerm(String item) {
        WebElement searchBar = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"twotabsearchtextbox\"]")));
        searchBar.clear();
        searchBar.sendKeys(item);
    }

    public void clickSearchButton() {
        WebElement searchButton = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//*[@id=\"nav-search-submit-button\"]")));
        searchButton.click();
    }

    public void verifyResultsPage(String item) {
        wait.until(ExpectedConditions.titleContains(item));
        System.out.println("Results page for " + item + " is displayed.");
    }

    public void printFirstFiveResults(String item) {
        List<WebElement> results = driver.findElements(By.xpath("(//*[@id=\"search\"]//h2/span)[position()<=5]"));
        System.out.println("First 5 " + item + " results:");
        for (int i = 0; i < results.size(); i++) {
            System.out.println((i + 1) + ". " + results.get(i).getText());
        }
    }

    public void closeBrowser() {
        if (driver != null) {
            driver.quit();
        }
    }
}
