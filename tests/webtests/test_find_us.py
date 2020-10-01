from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException


class TestFindUs(WebTestBase):
   
    def test_find_us_info(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        main_heading = "Hitta din väg hit"
        expected_subheadings = ["Med buss", "Med bil", "Med cykel", "Till fots"]

        find_us_elem = driver.find_element(By.ID, "find-us")
        subheading_elems = find_us_elem.find_elements(By.TAG_NAME, "h4")
        mainheading_elem = find_us_elem.find_element(By.TAG_NAME, "h3")

        self.assertEqual(len(subheading_elems), len(expected_subheadings))

        self.assertIn(main_heading, mainheading_elem.text)

        for subheading in subheading_elems:
            self.assertIn(subheading.text, expected_subheadings)
