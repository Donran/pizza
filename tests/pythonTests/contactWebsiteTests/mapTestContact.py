# Imports Selenium python module
from selenium import webdriver


class MapTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):

        print("")

        # Find map by id
        gMap = driver.find_element_by_id("gMap")
        # If not true, returns error
        print(gMap.get_attribute("src"))