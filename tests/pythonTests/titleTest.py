# Imports Selenium python module
from selenium import webdriver


class TitleTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find title h1
        titleText = driver.find_element_by_id("titleTextTest").text
        # Write title patch
        assert "PIZZERIA SANTOS" in titleText
        print(titleText)

        # Find the image picture by id
        titleImage = driver.find_element_by_id("titleImageTest")
        # Write image patch
        print(titleImage.get_attribute("url"))

        titleNumber = driver.find_element_by_id("titleNumberTest").text
        # Write title patch
        assert "0630-555-555" in titleNumber
        print(titleNumber)
