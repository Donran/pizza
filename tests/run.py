# Imports Selenium python module
from selenium import webdriver
# Imports the module for commandline arguments
import argparse
# Imports all of the classes from the files in the "pythonTests" directory
from webtests.menu_test import MenuTest
from webtests.info_test import InfoTest
from webtests.opening_hours_test import OpeningHoursTest
from webtests.title_test import TitleTest
from webtests.pictures_test import PicturesTest
from webtests.days_closed_test import DaysClosedTest
from webtests.logo_test import LogoTest
from webtests.order_test import OrderTest
from webtests.navbar_test import NavbarTest
from webtests.contact_tests.title_test_contact import TitleTestContact
from webtests.contact_tests.text_test_contact import TextTestContact
from webtests.contact_tests.info_test_contact import InfoTestContact
from webtests.contact_tests.map_test_contact import MapTestContact

# Initializing argument parser
parser = argparse.ArgumentParser(description='Test website')

# Choose between a local file or webhosted file
parser.add_argument("--source", '-s', default="web", choices=["local", "web"])
# The port to use when using localhost
parser.add_argument("--port", '-p', default="5500", help="The port to use when using localhost")
# Select the file to test
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

# Write chosen url(s)
print("Fetching from: " + url + file)
print("")

# Opens the chosen URL
driver.get(url + file)

# Calls all of the classes constructors
if file == "index.html":
    LogoTest(driver)
    NavbarTest(driver)
    TitleTest(driver)
    OpeningHoursTest(driver)
    DaysClosedTest(driver)
    MenuTest(driver)
    OrderTest(driver)
    PicturesTest(driver)
    InfoTest(driver)
elif file == "kontakt.html":
    LogoTest(driver)
    NavbarTest(driver)
    TitleTestContact(driver)
    TextTestContact(driver)
    InfoTestContact(driver)
    MapTestContact(driver)
