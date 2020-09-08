from selenium import webdriver


class TitleTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divPath = baseDivPath + "/div[@class='TitleContainer']"

        print("")

        # Find title h1
        imgURL: str = driver.find_element_by_xpath(divPath + "/div[@class='TitleImage']").value_of_css_property("background-image");
        print(imgURL.split('"', -1)[1])
        print(driver.find_element_by_xpath(divPath + "/h1[@class='Title']").text)
