from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TagPage:
    def __init__(self, driver: WebDriver):
        """Constructor for the TagPage

        Args:
            driver (WebDriver): Webdriver to be used
        """
        self.driver = driver
        self.more_filter_options_button = self.driver.find_element(by=By.XPATH, value="//button//span[contains(@data-text,'More')]")

    def sort_by_most_frequent(self) -> None:
        """Sorts the tag questions by most frequent
        """
        base_page = self.driver.find_element(By.TAG_NAME, "body")
        self.more_filter_options_button.click()
        more_popover_xpath = self.driver.find_element(by=By.XPATH, value="//*[@id='uql-more-popover']//*[contains(text(),'Frequent')]")
        more_popover_xpath.click()
        WebDriverWait(driver=self.driver, timeout=10).until(EC.staleness_of(base_page))
        WebDriverWait(driver=self.driver, timeout=10).until(lambda d: d.execute_script("return document.readyState") == "complete")


    def select_question_with_most_votes(self) -> None:
        """Selects the question with the most votes and navigates to it
        """
        questions = self.driver.find_elements(By.XPATH, "//*[@itemprop='upvoteCount']")
        best_element = max(questions, key=lambda e: int(e.text.strip()))
        best_value = int(best_element.text.strip())
        question_to_select = self.driver.find_element(By.XPATH, f"//span[normalize-space()={best_value}]/../../..//a[@class='s-link']")
        question_to_select.click()