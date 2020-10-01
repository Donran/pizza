from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException

class TestMapContact(WebTestBase):

    def test_map_contact(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        try:
            googleMap = driver.find_element(By.CLASS_NAME, "map")
        except NoSuchElementException:
            self.fail("No google maps elem found.")
