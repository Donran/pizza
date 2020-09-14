# Imports Selenium python module
from selenium import webdriver


class InfoTest:
    def __init__(self, driver: webdriver.Chrome):
        
        print("")

        # Find address by id
        footerAddressText = driver.find_element_by_id("footerAddress").text
        # If not true, returns error
        assert "Fjällgatan 32H" in footerAddressText
        print(footerAddressText)

        # Find address link 
        footerAddress = driver.find_element_by_id("footerAddress")
        print(footerAddress.get_attribute("href"))

        # Find zipcode by id
        footerZipCodeText = driver.find_element_by_id("footerZipCode").text
        # If not true, returns error
        assert "981 39 KIRUNA" in footerZipCodeText
        print(footerZipCodeText)

        # Find zipcode link
        footerZipCode = driver.find_element_by_id("footerZipCode")
        print(footerZipCode.get_attribute("href"))

        # Find email by id
        footerEmail = driver.find_element_by_id("footerEmail")
        print(footerEmail.get_attribute("href"))

        # Find phone number by id
        footerPhoneNumber = driver.find_element_by_id("footerPhoneNumber")
        print(footerPhoneNumber.get_attribute("href"))