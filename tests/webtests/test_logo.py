from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestLogo(WebTestBase):

    def test_logo(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find the logo picture by id
        logo = driver.find_element(By.ID, "logo")
        logo_src = logo.get_attribute("src")

        r = requests.get(logo_src)
        self.assertEqual(r.status_code, 200)
