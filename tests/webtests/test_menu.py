from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestMenu(WebTestBase):

    def test_menu(self):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        expected_menu = [
            ["Margarita", "ost", 80],
            ["Calzone", "skinka", 85],
            ["Vesuvio", "skinka", 85],
            ["Hawaii", "skinka, ananas", 90],
            ["Capricciosa", "skinka, champinjoner", 90],
            ["Pompei", "bacon, rödlök, ägg, curry", 90],
            ["La Casa", "skinka, champinjoner, räkor", 95],
            ["","",""],
            ["Extra topping", "", 5]
        ]

        menu = driver.find_element(By.CLASS_NAME, "menu")
        menu_items = menu.find_elements(By.TAG_NAME, "li")

        self.assertEqual(len(menu_items), len(expected_menu))

        for i in range(len(menu_items)):
            pizza_name = expected_menu[i][0]
            pizza_ingredients = expected_menu[i][1]
            pizza_price = str(expected_menu[i][2])
            self.assertIn(pizza_name, menu_items[i].text)
            self.assertIn(pizza_ingredients, menu_items[i].text)
            self.assertIn(pizza_price, menu_items[i].text)
