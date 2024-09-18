package locators;

import org.openqa.selenium.By;

public class Locators {
    public static By langaugeChangeButton = By.xpath("//*[@id=\"icp-nav-flyout\"]");
    public static By englishCheckbox = By.xpath("//*[@id=\"icp-language-settings\"]/div[2]/div/label/i");
    public static By hindiCheckbox = By.xpath("//*[@id=\"icp-language-settings\"]/div[3]/div/label/i");
    public static By saveChanges = By.xpath("//*[@id=\"icp-save-button\"]/span/input");
}
