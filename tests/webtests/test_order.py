from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def set_value_and_check(self, zipcode, driver, confirm_button, input_element):

        input_element.send_keys(zipcode)
        confirm_button.click()

        # Checks if input value outputs the correct message
        if driver.find_element(By.CLASS_NAME, "order-info").text != "Tyvärr kör vi inte ut inom detta område":
            return True
        else:
            return False

class TestOrder(WebTestBase):


    def test_valid_zipcode_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        order_button = driver.find_element(By.CLASS_NAME, "order-button")
        order_button.click()

        overlay = driver.find_element(By.CLASS_NAME, "order-overlay")

        input_element = overlay.find_element(By.TAG_NAME, "input")
        confirm_button = driver.find_element(By.CLASS_NAME, "order-confirm-button")

        input_element.send_keys("98139")
        confirm_button.click()

        self.assertIn("Vi levererar till dig", driver.page_source)

    def test_invalid_zipcode_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        order_button = driver.find_element(By.CLASS_NAME, "order-button")
        order_button.click()
        
        overlay = driver.find_element(By.CLASS_NAME, "order-overlay")

        input_element = overlay.find_element(By.TAG_NAME, "input")
        confirm_button = driver.find_element(By.CLASS_NAME, "order-confirm-button")

        input_element.send_keys("123456")
        confirm_button.click()

        self.assertIn("Tyvärr kör vi inte ut inom detta område", driver.page_source)

    def test_keyshortcuts_works(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        order_button = driver.find_element(By.CLASS_NAME, "order-button")
        order_button.click()

        overlay = driver.find_element(By.CLASS_NAME, "order-overlay")

        input_element = overlay.find_element(By.TAG_NAME, "input")
        input_element.send_keys("98139")
        input_element.send_keys(Keys.RETURN)

        self.assertIn("Vi levererar till dig", driver.page_source)

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

        self.assertEqual(overlay.get_attribute("data-state"), "hidden")


