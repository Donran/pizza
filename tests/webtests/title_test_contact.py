from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException


class TestTitleContact(WebTestBase):

    def test_title_contact(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/kontakt.html")

        title = driver.find_element(By.ID, "titleTextTest").text

        self.assertIn("PIZZERIA SANTOS", title)
