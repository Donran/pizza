# Imports Selenium python module
from selenium import webdriver

class DaysClosedTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        ulPath = baseDivPath + "/div[@id='Hours']/ul[@id='closedDays']"
        # Gets a list of all li in the ul
        itemList: list = driver.find_elements_by_xpath(ulPath + "/li")
        # Prints an error message if the closed dates are not found
        assert len(itemList) != 0
        # Find closed dates
        for index in range(len(itemList)):
            date = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[1]").text
            status = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            print(date + ": " + status)
