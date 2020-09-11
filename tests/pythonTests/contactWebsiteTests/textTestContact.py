# Imports Selenium python module
from selenium import webdriver


class TextTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        DivPath = baseDivPath + "/h2[1]"

        print("")

        # Gets the text of the h2
        text = driver.find_element_by_xpath(DivPath).text
        # If not true, returns error
        assert "HITTA HIT TILL OSS!" in text
        print(text)
