from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestOrder(WebTestBase):

    def test_valid_zipcode_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        zipcode_field = driver.find_element(By.CLASS_NAME, "zipcode-field")

        input_element = zipcode_field.find_element(By.ID, "order-form")
        confirm_button = driver.find_element(By.CLASS_NAME, "order-confirm-button")

        input_element.send_keys("98139")
        confirm_button.click()

        self.assertIn("Vi levererar till dig", driver.page_source)

    def test_invalid_zipcode_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        zipcode_field = driver.find_element(By.CLASS_NAME, "zipcode-field")

        input_element = zipcode_field.find_element(By.ID, "order-form")
        confirm_button = driver.find_element(By.CLASS_NAME, "order-confirm-button")

        input_element.send_keys("123456")
        confirm_button.click()

        self.assertIn("Tyvärr kör vi inte ut inom detta område", driver.page_source)

    def test_keyshortcuts_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        zipcode_field = driver.find_element(By.CLASS_NAME, "zipcode-field")

        input_element = zipcode_field.find_element(By.ID, "order-form")
        input_element.send_keys("98139")
        input_element.send_keys(Keys.RETURN)

        self.assertIn("Vi levererar till dig", driver.page_source)

