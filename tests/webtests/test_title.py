from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestTitle(WebTestBase):

    def test_title(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find title by id
        titleText = driver.find_element(By.ID, "titleTextTest").text
        # If not true, returns error
        self.assertIn("PIZZERIA SANTOS", titleText)

        # Find title image by id
        titleImage = driver.find_element(By.ID, "titleImageTest")

        # Find title phone number by id
        titlePhoneNumber = driver.find_element(By.ID, "titlePhoneNumberTest").text
        # If not true, returns error
        self.assertIn("0630-555-555", titlePhoneNumber)

        # Find title address by id
        titleAddress = driver.find_element(By.ID, "titleAddressTest").text
        # If not true, returns error
        self.assertIn("Fjällgatan 32H", titleAddress)
