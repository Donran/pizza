from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase
from selenium.common.exceptions import NoSuchElementException

def set_value_and_check(self, value, driver, confirmButton, inputElement):
        # Change the value of the input element to a valid zip-code
        driver.execute_script(
            "arguments[0].setAttribute('value', arguments[1])", inputElement, value)
        confirmButton.click()

        # Checks if input value outputs the correct message
        if driver.find_element(By.ID, "orderStatus").text != "Vi levererar inte till dig":
            return True
        else:
            return False

class TestOrder(WebTestBase):

    def test_order(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Find order button by id
        orderButton = driver.find_element(By.ID, "orderButton")
        self.assertEqual(orderButton.text, "UTKÖRNING")

        try:
            # Find order overlay by id
            overlay = driver.find_element(By.ID, "orderOverlay")
        except NoSuchElementException:
            self.fail("Could not find order overlay.")

        orderButton.click()
        self.assertEqual(overlay.get_attribute("data-state"), "visible")

        # Find input by id
        inputElement = driver.find_element(By.ID, "orderInput")
        # Find confirm button by id
        confirmButton = driver.find_element(By.ID, "orderConfirmButton")
        # Sets value of input to a zip code
        self.assertEqual(set_value_and_check(self, "98139", driver, confirmButton, inputElement), True)
        self.assertEqual(set_value_and_check(self, "89488", driver, confirmButton, inputElement), False)
