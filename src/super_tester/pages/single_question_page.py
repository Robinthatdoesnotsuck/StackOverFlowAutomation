from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

class QuestionPage():

    def __init__(self, driver: WebDriver) -> None:
        """Constructor for the Question Page

        Args:
            driver (WebDriver): WebDriver to be used
        """
        self.driver = driver
        self.author_with_highest_score = self.driver.find_element(by=By.XPATH, value="//div[@data-highest-scored=1]//div[@class='user-details' and @itemprop='author']//a")

    def author_from_most_voted_answer(self) -> str:
        """Gets the author name from the most voted answer

        Returns:
            str: Author name
        """
        return self.author_with_highest_score.text