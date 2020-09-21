from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
import requests

class TestNavbar(WebTestBase):

    def test_navbar(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        navbar = driver.find_element(By.CLASS_NAME, "navbar")
        navlinks = navbar.find_elements(By.TAG_NAME, "a")

        for nav_link in navlinks:
            nav_link_href = nav_link.get_attribute("href")
            r = requests.get(nav_link_href)
            self.assertEqual(r.status_code, 200)