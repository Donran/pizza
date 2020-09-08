from selenium import webdriver


class DaysClodesTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        itemList: list = driver.find_elements_by_xpath(
            baseDivPath + "/div[@id='hours']/ul[@id='closedDays']")
        if len(itemList) != 0:
            for item in itemList:
                print(item.text)
        else:
            print("ERROR")
