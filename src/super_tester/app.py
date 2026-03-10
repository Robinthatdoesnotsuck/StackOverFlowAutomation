from selenium import webdriver
from src.super_tester.pages.questions_page import QuestionsPage
from src.super_tester.pages.search_tags_page import SearchTagsPage
from src.super_tester.pages.tag_page import TagPage
from src.super_tester.pages.single_question_page import QuestionPage


def main():
    driver = webdriver.Firefox()
    driver.get("https://stackoverflow.com")
    questionsPage = QuestionsPage(driver=driver)
    questionsPage.go_to_search_by_tags_page()
    searchTagsPage = SearchTagsPage(driver=driver)
    searchTagsPage.search_for_tag("python")
    searchTagsPage.select_tag_with_sub_option(sub_option="3.6")
    tagPage = TagPage(driver=driver)
    tagPage.sort_by_most_frequent()
    tagPage.select_question_with_most_votes()
    singleQuestionPage = QuestionPage(driver=driver)
    print(singleQuestionPage.author_from_most_voted_answer())
    driver.quit()

if __name__ == "__main__":
    main()