from selenium import webdriver


class FooterTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divPath = baseDivPath + "/div[@class='footer']"

        print("")

        # Find title h1
        images: list = driver.find_elements_by_xpath(divPath + "/img[@class='pizzaFooter']")
        for item in images:
            print(item.get_attribute("src"))