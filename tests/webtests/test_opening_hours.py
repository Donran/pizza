from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestOpeningHours(WebTestBase):

    def test_opening_hours(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        expected_open_hours = [
            "Mån-Tors 10-22",
            "Fredagar 10-23",
            "Lördagar 12-23",
            "Söndagar 12-20"
        ]

        # Find opening hours list by id
        opening_hours = driver.find_element(By.ID, "openingHours")
        opening_hours_arr = opening_hours.find_elements(By.TAG_NAME, "li")

        self.assertEqual(len(expected_open_hours), len(opening_hours_arr))

        for i in range(len(expected_open_hours)):
            self.assertIn(expected_open_hours[i], opening_hours_arr[i].text.replace("\n", " "))
