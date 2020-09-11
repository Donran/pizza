# Imports Selenium python module
from selenium import webdriver


class MapTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divPath = baseDivPath + "/div[@class='contact']/div[@class='map']"

        print("")

        # Find title h1
        images: list = driver.find_elements_by_xpath(divPath + "/iframe")
        # If not true, returns error
        assert len(images) != 0
        # Loops through all of the images and prints the src
        for item in images:
            print(item.get_attribute("src"))