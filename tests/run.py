# Imports Selenium python module
from selenium import webdriver
# Imports all of the classes from the files in the "pythonTests" directory
from pythonTests.menuTest import MenuTest
from pythonTests.infoTest import InfoTest
from pythonTests.openingHoursTest import OpeningHoursTest
from pythonTests.titleTest import TitleTest
from pythonTests.picturesTest import PicturesTest
from pythonTests.daysClosedTest import DaysClosedTest
from pythonTests.logoTest import LogoTest
from pythonTests.orderTest import OrderTest
from pythonTests.contactWebsiteTests.titleTestContact import TitleTestContact
from pythonTests.contactWebsiteTests.textTestContact import TextTestContact
from pythonTests.contactWebsiteTests.infoTestContact import InfoTestContact
from pythonTests.contactWebsiteTests.mapTestContact import MapTestContact

# Configures google web options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Ask what host you want
print("""1. localhost
2. public website""")
choice = input("Choose: ")

# Configures two alternatives
url = ""
if choice == "1":
    port = input("Choose port (default should be 5500): ")
    url = "http://localhost:" + port + "/public/"
elif choice == "2":
    url = "https://fantastic4group.gitlab.io/pizza-website/"

print("""1. index.html
2. kontakt.html""")
subSiteChoice = input("Choice: ")
if int(subSiteChoice) == 1:
    subsite = "index.html"
elif int(subSiteChoice) == 2:
    subsite = "kontakt.html"

print("Fetching from: " + url + subsite)

# Opens the chosen URL
driver.get(url + subsite)

# Creates a variable with the base path to make the code more compact and easier to read
baseDivPath = "/html/body/div[@class='contentDiv']"

# Calls all of the classes constructors
if subsite == "index.html":
    LogoTest(driver, baseDivPath)
    InfoTest(driver, baseDivPath)
    OpeningHoursTest(driver, baseDivPath)
    DaysClosedTest(driver, baseDivPath)
    TitleTest(driver, baseDivPath)
    MenuTest(driver, baseDivPath)
    PicturesTest(driver, baseDivPath)
    OrderTest(driver, baseDivPath)
elif subsite == "kontakt.html":
    LogoTest(driver, baseDivPath)
    TitleTestContact(driver, baseDivPath)
    TextTestContact(driver, baseDivPath)
    InfoTestContact(driver, baseDivPath)
    MapTestContact(driver, baseDivPath)
    pass
