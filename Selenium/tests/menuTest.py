from selenium import webdriver


class MenuTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        ulPath = baseDivPath + "/ul[@id='menu']"
        # Find menu h2
        driver.find_element_by_xpath(
            "/html/body/div[@class='ContentDiv']/h2[contains(text(),'Meny')]")

        # Find menu entries
        for index in range(len(driver.find_elements_by_xpath(ulPath + "/li"))):
            text = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[1]").text
            price = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            print("Found item " + text)
            print("With price: " + price)
            print("")
