# Imports Selenium python module
from selenium import webdriver


class InfoTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divpath = baseDivPath + "/div[@id='InfoDiv']"
        print("")
        # Find address
        address = driver.find_elements_by_xpath(
            divpath + "/div[@id='addressDiv']/a[@href='https://goo.gl/maps/2aqFdNDscvCgKKQR9']")
        # If not true, returns error
        print(address)
        assert len(address) != 0
        for item in range(len(address)):
             print(address[item].text)

        # Find email
        address = driver.find_element_by_xpath(
            divpath + "/div[@id='otherInfoDiv']/a[@href='mailto:info@fantastic4group.gitlab.io']").text
        # If not true, returns error
        assert address != ""
        print(address)

        # Find phone number
        address = driver.find_element_by_xpath(
            divpath + "/div[@id='otherInfoDiv']/a[@href='tel:0630-555-555']").text
        # If not true, returns error
        assert address != ""
        print(address)
