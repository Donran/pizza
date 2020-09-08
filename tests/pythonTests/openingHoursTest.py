from selenium import webdriver


class OpeningHoursTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        print("")
        ulPath = baseDivPath + "/div[@id='InfoDiv']/ul[@id='openingHours']"

        # Find menu entries
        for index in range(len(driver.find_elements_by_xpath(ulPath + "/li"))):
            day = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[1]").text
            time = driver.find_element_by_xpath(
                ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            print(day + ": " + time)
