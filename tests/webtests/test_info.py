import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException


class TestInfo(WebTestBase):

    @classmethod
    def setUpClass(self):
        super(TestInfo, self).setUpClass()
        self.address = "Fjällgatan 32H"
        self.zipcode = "981 39 KIRUNA"
        self.phonenumber = "0630‑555‑555"
        self.email = "info@fantastic4group.gitlab.io"

    # Tests if info exists on page index.
    def test_info_exists_index(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Testing if all info exists on page
        self.assertIn(self.address, driver.page_source)
        self.assertIn(self.zipcode, driver.page_source)
        self.assertIn(self.phonenumber, driver.page_source)
        self.assertIn(self.email, driver.page_source)

    # Tests if info exists in the footer on page index.
    def test_info_in_footer_index(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        try:
            footer = driver.find_element(By.ID, "footer")
        except NoSuchElementException:
            self.fail("Could not find footer")

        footer_text = footer.text
        self.assertIn(self.address, footer_text)
        self.assertIn(self.zipcode, footer_text)
        self.assertIn(self.phonenumber, footer_text)
        self.assertIn(self.email, footer_text)
