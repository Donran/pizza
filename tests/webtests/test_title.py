from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestTitle(WebTestBase):

    def test_title(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        #Find element by class
        header_text = driver.find_element(By.CLASS_NAME, "header-text").text
        #Looking for text in header_text
        self.assertIn("Välkommen till", header_text)
        self.assertIn("Pizzeria Santos", header_text)
        #Find element by class
        header_logo = driver.find_element(By.CLASS_NAME, "header-logo")
        #Find element by tag
        logo_img = header_logo.find_element(By.TAG_NAME, "img")
        #Save source attribute in variable
        src = logo_img.get_attribute("src")
        #Looking for correct logo in src
        self.assertIn("/assets/svg/icon4.svg", src)
        


