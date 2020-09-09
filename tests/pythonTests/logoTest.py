# Imports Selenium python module
from selenium import webdriver

class LogoTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divPath = baseDivPath + "/div[@class='Header']"
        print("")

        #Find the logo picture
        logo: list = driver.find_element_by_xpath(divPath + "/img[1]")
        # If not true, returns error
        assert "/assets/Logo.svg" in logo.get_attribute("src")
        print(logo.get_attribute("src"))
