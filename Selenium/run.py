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

driver.get("http://localhost:5500/public/")

baseDivPath = "/html/body/div[@class='ContentDiv']"


MenuTest(driver, baseDivPath)

InfoTest(driver, baseDivPath)

OpeningHoursTest(driver, baseDivPath)

TitleTest(driver, baseDivPath)

FooterTest(driver, baseDivPath)

