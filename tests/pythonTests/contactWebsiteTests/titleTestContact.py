# Imports Selenium python module
from selenium import webdriver


class TitleTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):

        print("")

        # Find the title by id
        title = driver.find_element_by_id("title").text
        # If not true, returns error
        assert "PIZZERIA SANTOS" in title
        print(title)
