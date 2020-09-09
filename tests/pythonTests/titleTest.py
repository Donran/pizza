# Imports Selenium python module
from selenium import webdriver


class TitleTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divPath = baseDivPath + "/div[@class='TitleContainer']"

        print("")

        # Find title h1
        imgURL: str = driver.find_element_by_xpath(divPath + "/div[@class='TitleImage']").value_of_css_property("background-image")
        # Gets the url of the image
        url: str = imgURL.split('"', -1)[1]
        # Gets the title of the h1
        title = driver.find_element_by_xpath(divPath + "/h1[@class='Title']").text
        # If not true, returns error
        assert "assets/bild4.jpg" in url
        assert "PIZZERIA SANTOS" in title
        print(url)
        print(title)
