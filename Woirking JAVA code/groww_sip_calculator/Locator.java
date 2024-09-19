
package locators;

import org.openqa.selenium.By;

public class Locators {
    public static By monthlyInvestment = By.xpath("//*[@id=\"MONTHLY_INVESTMENT\"]");
    public static By expectedReturnRate = By.xpath("//*[@id=\"RETURN_RATE\"]");
    public static By timePeriod = By.xpath("//*[@id=\"TIME_PERIOD\"]");
    public static By investmentAmount = By.xpath("//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/span/span");
    public static By estReturn = By.xpath("//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/span/span");
    public static By totalValue = By.xpath("//*[@id=\"root\"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[3]/div[2]/span/span");
}
