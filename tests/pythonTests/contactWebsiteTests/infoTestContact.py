# Imports Selenium python module
from selenium import webdriver


class InfoTestContact:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        DivPath = baseDivPath + "/div[@class='contact']/div[@id='InfoDiv']/a"

        print("")

        # Gets the text of the h2
        text = driver.find_element_by_xpath(DivPath + "[1]").text
        # If not true, returns error
        assert "Fjällgatan 32H" in text
        print(text)

        # Gets the text of the h2
        text = driver.find_element_by_xpath(DivPath + "[2]").text
        # If not true, returns error
        assert "981 39 KIRUNA" in text
        print(text)

        # Find email
        address = driver.find_element_by_xpath(
            baseDivPath + "/div[@class='contact']/div[@id='InfoDiv']/a[@href='mailto:info@fantastic4group.gitlab.io']").text
        #If not true, returns error
        assert address != ""
        print(address)

        # Find phone number
        address = driver.find_element_by_xpath(
           baseDivPath + "/div[@class='contact']/div[@id='InfoDiv']/a[@href='tel:0630-555-555']").text
        #If not true, returns error
        assert address != ""
        print(address)
