from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException


class TestFindUs(WebTestBase):
   
    def test_find_us_info(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/kontakt.html")

        expected_headings = ["Hitta din väg hit", "Med buss", "Med bil", "Med cykel", "Till fots"]

        text_border_elem = driver.find_element(By.CLASS_NAME, "text-border")
        heading_elems = text_border_elem.find_elements(By.TAG_NAME, "h2")
        
        self.assertEqual(len(heading_elems), len(expected_headings))

        for heading in heading_elems:
            self.assertIn(heading.text, expected_headings)
