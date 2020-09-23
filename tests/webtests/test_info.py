from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException


class TestInfo(WebTestBase):

    def test_info(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find address by id
        footerAddressText = driver.find_element(By.ID, "address").text
        # If not true, returns error
        self.assertIn("Fjällgatan 32H", footerAddressText)

        # Find address link by id
        footerAddress = driver.find_element(By.ID, "address")

        # Find zipcode by id
        footerZipCodeText = driver.find_element(By.ID, "zipCode").text
        # If not true, returns error
        self.assertIn("981 39 KIRUNA", footerZipCodeText)

        try:
            # Find zipcode link by id
            driver.find_element(By.ID, "zipCode")
        except NoSuchElementException:
            self.fail("Couldnt find zipcode")

        try:
            # Find email by id
           driver.find_element(By.ID, "email")
        except NoSuchElementException:
            self.fail("Couldnt find email")

        try:
            # Find phone number by id
            driver.find_element(By.ID, "phoneNumber")
        except NoSuchElementException:
            self.fail("Couldnt find phonenumber")
