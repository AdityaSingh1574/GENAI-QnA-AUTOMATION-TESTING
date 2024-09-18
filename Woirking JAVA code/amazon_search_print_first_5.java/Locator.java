package locators;

import org.openqa.selenium.By;

public class Locators {
    public static By searchBar = By.xpath("//*[@id=\"twotabsearchtextbox\"]");
    public static By searchButton = By.xpath("//*[@id=\"nav-search-submit-button\"]");
    public static By searchResult1 = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span");
    public static By searchResult2 = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span");
    public static By searchResult3 = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span");
    public static By searchResult4 = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span");
    public static By searchResult5 = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span");
}
