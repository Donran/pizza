from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestPictures(WebTestBase):

    def test_pictures(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find pizza images by class name
        images_test = driver.find_elements(By.CLASS_NAME, "pizzaPictures")
        # For loop that loops through all the items in the div and prints their source
        for item in images_test:
            img_src = item.get_attribute("src")
            r = requests.get(img_src)
            self.assertEqual(r.status_code, 200)