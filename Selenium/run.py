import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.menuTest import MenuTest
from tests.infoTest import InfoTest
from tests.openingHoursTest import OpeningHoursTest
from tests.titleTest import TitleTest
from tests.footerTest import FooterTest

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

print("""1. localhost
2. public website""")
choice = input("Choose: ")

url = ""
if choice == "1":
    port = input("Choose port (default should be 5500): ")
    url = "http://localhost:" + port + "/public/"
elif choice == "2":
    url = "https://fantastic4group.gitlab.io/pizza-website/"

print("Fetching from: " + url)

driver.get(url)

baseDivPath = "/html/body/div[@class='ContentDiv']"

InfoTest(driver, baseDivPath)
OpeningHoursTest(driver, baseDivPath)
TitleTest(driver, baseDivPath)
MenuTest(driver, baseDivPath)
FooterTest(driver, baseDivPath)
