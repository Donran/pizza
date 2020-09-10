from selenium import webdriver


def setValueAndCheck(self, value: int, driver: webdriver.Chrome):
    # Change the value of the input element to a valid zip-code
    driver.execute_script(
        "arguments[0].setAttribute('value', arguments[1])", self.inputElement, value)
    self.confirmButton.click()
    # Check if the zip-code is valid or not
    assert driver.find_element_by_id(
        "orderStatus").text != "Vi levererar inte till dig"
    print("Zip Code test succeeded")


class OrderTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        # Find order button
        orderButton = driver.find_element_by_id("orderButton")
        assert orderButton.text == "BESTÄLL"
        print(orderButton.text)
        # Find order overlay
        overlay = driver.find_element_by_id("orderOverlay")
        assert overlay
        orderButton.click()
        assert overlay.get_attribute("data-state") == "visible"

        self.inputElement = driver.find_element_by_id("orderInput")
        self.confirmButton = driver.find_element_by_id("orderConfirmButton")
        setValueAndCheck(self, "98139", driver)
