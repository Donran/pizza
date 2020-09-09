# Imports Selenium python module
from selenium import webdriver


class InfoTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divpath = baseDivPath + "/div[@id='InfoDiv']"
        print("")
        # Find address
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='https://goo.gl/maps/2aqFdNDscvCgKKQR9']").text
        # If not true, returns error
        assert address != ""
        print(address)

        # Find email
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='mailto:info@fantastic4group.gitlab.io']").text
        # If not true, returns error
        assert address != ""
        print(address)

        # Find phone number
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='tel:0630-555-555']").text
        # If not true, returns error
        assert address != ""
        print(address)
