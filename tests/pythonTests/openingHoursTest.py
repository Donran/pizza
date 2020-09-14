# Imports Selenium python module
from selenium import webdriver


class OpeningHoursTest:
    def __init__(self, driver: webdriver.Chrome):

        print("")
        
        # Find the logo picture by id
        openingHours = driver.find_elements_by_id("openingHours")

        for item in openingHours:
            print(item.text)
        # Write logos patch
        # print(openingHours)







        #for index in range(len(driver.find_elements_by_xpath(ulPath + "/li"))):
         #   day = driver.find_element_by_xpath(
          #      ulPath + "/li[" + str(index + 1) + "]/span[1]").text
           # time = driver.find_element_by_xpath(
            #    ulPath + "/li[" + str(index + 1) + "]/span[2]").text
            #print(day + ": " + time)
