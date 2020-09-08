from selenium import webdriver


class InfoTest:
    def __init__(self, driver: webdriver.Chrome, baseDivPath: str):
        divpath = baseDivPath + "/div[@id='InfoDiv']"
        print("")
        # Find address
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='https://goo.gl/maps/2aqFdNDscvCgKKQR9']").text
        print(address)

        # Find email
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='mailto:info@fantastic4group.gitlab.io']").text
        print(address)

        # Find phone number
        address = driver.find_element_by_xpath(
            divpath + "/a[@href='tel:0630-555-555']").text
        print(address)