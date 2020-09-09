from selenium import webdriver


class OrderTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        orderButton = driver.find_element_by_id("orderButton")
        assert orderButton.text == "BESTÄLL"
        print(orderButton.text)
        overlay= driver.find_element_by_id("orderOverlay")
        assert overlay