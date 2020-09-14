# Imports Selenium python module
from selenium import webdriver


class InfoTestContact:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        # Find the text by id
        text = driver.find_element_by_id("adress1").text
        # If not true, returns error
        assert "Fjällgatan 32H" in text
        print(text)

        # Find the text by id
        text = driver.find_element_by_id("adress2").text
        # If not true, returns error
        assert "981 39 KIRUNA" in text
        print(text)

        print("")

        # Find the email by id
        text = driver.find_element_by_id("email")
        # Write emails patch
        print(text.get_attribute("href"))

        print("")

        # Find the mobile by id
        adress = driver.find_element_by_id("tele")
        # Write mobiles patch
        print(adress.get_attribute("href"))
