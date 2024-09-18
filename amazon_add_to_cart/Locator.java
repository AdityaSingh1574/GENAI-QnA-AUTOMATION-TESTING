package locators;

import org.openqa.selenium.By;

public class Locators {
    public static By searchBar = By.xpath("//*[@id=\"twotabsearchtextbox\"]");
    public static By searchButton = By.xpath("//*[@id=\"nav-search-submit-button\"]");
    public static By firstSearchResult = By.xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span");
    public static By addToCart = By.xpath("//*[@id=\"add-to-cart-button\"]");
    public static By cartCounter = By.xpath("//*[@id=\"nav-cart-count\"]");
}
