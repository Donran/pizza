from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestTitle(WebTestBase):

    def test_title(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find title by id
        header_text = driver.find_element(By.CLASS_NAME, "header-title").text
        # If not true, returns error
        self.assertIn("PIZZERIA SANTOS", header_text)

        header_information = driver.find_elements(By.CLASS_NAME, "header-information")

        # Find title phone number by id
        header_phonenumber = header_information[0].text
        # If not true, returns error
        self.assertIn("0630-555-555", header_phonenumber)

        # Find title address by id
        header_address = header_information[2].text
        # If not true, returns error
        self.assertIn("Fjällgatan 32H", header_address)

