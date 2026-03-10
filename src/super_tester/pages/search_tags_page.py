import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchTagsPage:

    def __init__(self, driver: WebDriver) -> None:
        """Constructor for the SearchTagsPage

        Args:
            driver (WebDriver): WebDriver to be used
        """
        self.driver = driver
        self.filter_tag_input = self.driver.find_element(by=By.ID, value="tagfilter")
        self.tag_searched = ""
    
    def search_for_tag(self, search_tag: str) -> None:
        """Searches for a general tag in the page

        Args:
            search_tag (str): Tag to be search
        """
        self.filter_tag_input.send_keys(search_tag)
        time.sleep(3)
        self.filter_tag_input.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        self.tag_searched = search_tag


    def select_tag_with_sub_option(self, sub_option: str) -> None:
        """Selects a tag with a sub-option

        Args:
            sub_option (str): sub-option for the tag
        """
        sub_option_link = self.driver.find_element(by=By.XPATH, value=f"//div//a[contains(., '{self.tag_searched}-{sub_option}')]")
        sub_option_link.click()