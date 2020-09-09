# Imports Selenium python module
from selenium import webdriver


class MenuTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        ulPath = baseDivPath + "/ul[@id='menu']"
        print("")
        # Find menu h2
        driver.find_element_by_xpath(
            "/html/body/div[@class='ContentDiv']/h2[contains(text(),'MENY')]")

        # If not true, returns error
        assert len(driver.find_elements_by_xpath(ulPath + "/li")) != 0
        # Find menu entries
        for index in range(len(driver.find_elements_by_xpath(ulPath + "/li"))):
            text = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[1]").text
            price = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            # Asserts that the menu text and the price isn't an empty file
            assert text != ""
            assert price != ""
            print("Found item " + text)
            print("With price: " + price)
            print("")
