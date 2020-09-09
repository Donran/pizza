# Imports Selenium python module
from selenium import webdriver


class OpeningHoursTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        ulPath = baseDivPath + "/div[@id='Hours']/ul[@id='openingHours']"

        
        # If not true, returns error
        assert len(driver.find_elements_by_xpath(ulPath + "/li")) != 0
        # Finds menu entries and prints them
        for index in range(len(driver.find_elements_by_xpath(ulPath + "/li"))):
            day = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[1]").text
            time = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            print(day + ": " + time)
