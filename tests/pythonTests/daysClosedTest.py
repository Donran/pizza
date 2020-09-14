# Imports Selenium python module
from selenium import webdriver

class DaysClosedTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")

        #Find the closed day list by id
        closedDays = driver.find_elements_by_id("closedDays")
        # For loop that loops through all the items in the list and prints them
        for item in closedDays:
            print(item.text)
