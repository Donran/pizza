from selenium import webdriver


class OrderTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        # Find order button
        orderButton = driver.find_element_by_id("orderButton")
        assert orderButton.text == "BESTÄLL"
        print(orderButton.text)
        # Find order overlay
        overlay= driver.find_element_by_id("orderOverlay")
        assert overlay
        orderButton.click()
        # assert overlay.get_attribute("data-state") == "visible"
        
        inputElement = driver.find_element_by_id("orderInput")
        confirmButton = driver.find_element_by_id("orderConfirmButton")