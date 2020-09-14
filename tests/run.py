# Imports Selenium python module
from selenium import webdriver
# Imports the module for commandline arguments
import argparse
# Imports all of the classes from the files in the "pythonTests" directory
from pythonTests.menuTest import MenuTest
from pythonTests.infoTest import InfoTest
from pythonTests.openingHoursTest import OpeningHoursTest
from pythonTests.titleTest import TitleTest
from pythonTests.picturesTest import PicturesTest
from pythonTests.daysClosedTest import DaysClosedTest
from pythonTests.logoTest import LogoTest
from pythonTests.orderTest import OrderTest
from pythonTests.navbarTest import NavbarTest
from pythonTests.contactWebsiteTests.titleTestContact import TitleTestContact
from pythonTests.contactWebsiteTests.textTestContact import TextTestContact
from pythonTests.contactWebsiteTests.infoTestContact import InfoTestContact
from pythonTests.contactWebsiteTests.mapTestContact import MapTestContact

parser = argparse.ArgumentParser(description='Test website')

parser.add_argument("--source", '-s', default="web", choices=["local", "web"])
parser.add_argument("--port", '-p', default="5500", help="The port to use when using localhost")
parser.add_argument("--file", '-f', default="index.html", help="Select the file to test")
args = vars(parser.parse_args())

source = args["source"]
port = args["port"]
file = args["file"]

# Configures google web options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Configures two alternatives
url = ""
if str(source) == "local":
    url = "http://localhost:" + port + "/public/"
elif str(source) == "web":
    url = "https://fantastic4group.gitlab.io/pizza-website/"


print("Fetching from: " + url + file)
print("")

# Opens the chosen URL
driver.get(url + file)

# Calls all of the classes constructors
if file == "index.html":
    LogoTest(driver) 
    TitleTest(driver)
    OpeningHoursTest(driver)
    DaysClosedTest(driver)
    MenuTest(driver)
    PicturesTest(driver)
    #OrderTest(driver)
    #InfoTest(driver)
    NavbarTest(driver)
elif file == "kontakt.html":
    LogoTest(driver)
    NavbarTest(driver)
    TitleTestContact(driver)
    TextTestContact(driver)
    InfoTestContact(driver)
    MapTestContact(driver)
