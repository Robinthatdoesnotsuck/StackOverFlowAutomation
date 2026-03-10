from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

class QuestionsPage:
    def __init__(self, driver: WebDriver) -> None:
        """Constructor for the general questions page

        Args:
            driver (WebDriver): Webdriver to be used
        """
        self.driver = driver
        self.tags_link = self.driver.find_element(by=By.XPATH, value = "//li[contains(@class,'ps-relative')]//a//div[contains(.,'Tags')]")
    
    def go_to_search_by_tags_page(self) -> None:
        """Navigates to the tags page from the side menu
        """
        self.tags_link.click()