# Imports Selenium python module
from selenium import webdriver


class TitleTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        imageDivPath = baseDivPath + "/div[@class='TitleContainer']"

        print("")

        # Gets the title of the h1
        title = driver.find_element_by_xpath(imageDivPath + "/h1[@class='Title']").text
        # If not true, returns error
        assert "PIZZERIA SANTOS" in title
        print(title)
