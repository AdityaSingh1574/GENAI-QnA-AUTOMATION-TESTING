package locators;

import org.openqa.selenium.By;

public class Locators {
    public static By flight_from_input_field = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/input");
    public static By delhi_selection_button = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/li");
    public static By flight_to_input_field = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/input");
    public static By mumbai_selection_button = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/li");
    public static By departure_date_button = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div/div/p[2]");
    public static By exact_date_button = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/button[12]");
    public static By search_button = By.xpath("/html/body/main/div[2]/div[1]/div[3]/div[2]/button/svg/path");
    public static By price_low_to_high_button = By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/span/span");
    public static By lowest_price_flight_book_button = By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/button");
}