from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://localhost:5500/public/")

try:
    pizza1 = driver.find_element_by_id("pizza_Margarita")
    print(pizza1)
except print(0):
    pass