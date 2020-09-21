from selenium import webdriver
from selenium.webdriver.common.by import By
from web_test_base import WebTestBase

class TestDaysClosed(WebTestBase):

    def check_order_closed_dates(self, month: int, date: int, expectedOrder: list):
        driver = self.driver
        driver.get(self.WEBSITE_URL)

        # Executes the JS reordering script with a custom month and date
        driver.execute_script(
            "reorderListByClosestDate(new Date(2020," + str(month - 1) + "," + str(date) + "))")
        # Gets the current sorted order from the classes closedDate
        websiteOrder = list(map(
            lambda date: date.text, self.driver.find_elements(By.CLASS_NAME, "closedDate")))
        # Asserts that the expected order and the website order is the same
        self.assertEqual(expectedOrder, websiteOrder)

    def test_days_closed(self):
        # Runs the function check_order_closed_dates that reorders the list with the specified date and checks if it's sorted correctly
        self.check_order_closed_dates(12, 24, ['24 december', '25 december',
                                            '26 december', '6 januari', '1 maj'])

        self.check_order_closed_dates(12, 25, ['25 december', '26 december',
                                            '6 januari', '1 maj', '24 december'])

        self.check_order_closed_dates(12, 26, ['26 december', '6 januari',
                                            '1 maj', '24 december', '25 december'])

        self.check_order_closed_dates(12, 27, ['6 januari', '1 maj',
                                            '24 december', '25 december', '26 december'])

        self.check_order_closed_dates(1, 6, ['6 januari', '1 maj',
                                          '24 december', '25 december', '26 december'])

        self.check_order_closed_dates(1, 7, ['1 maj', '24 december',
                                          '25 december', '26 december', '6 januari'])

        self.check_order_closed_dates(5, 1, ['1 maj', '24 december',
                                          '25 december', '26 december', '6 januari'])

        self.check_order_closed_dates(5, 2, ['24 december', '25 december',
                                          '26 december', '6 januari', '1 maj'])
