from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException

class TestInfoContact(WebTestBase):

    def test_info_contact(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL+"/kontakt.html")

        # Find address by id
        text = driver.find_element(By.ID, "address").text
        # If not true, returns error
        self.assertIn("Fjällgatan 32H", text)

        # Find zipcode by id
        text = driver.find_element(By.ID, "zipCode").text
        # If not true, returns error
        self.assertIn("981 39 KIRUNA", text)

        # Find email by id
        text = driver.find_element(By.ID, "email")

        # Find phone number by id
        try:
            driver.find_element(By.ID, "phoneNumber")
        except NoSuchElementException:
            self.fail("No phonenumber found.")