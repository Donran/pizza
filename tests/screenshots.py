#!/usr/bin/env python3
import os
import shutil
import tracemalloc
from selenium import webdriver
from time import sleep

# Trace memory allocations in case of errors
tracemalloc.start()

class ScreenshotTest():

    def setUp(self):
        # Selects the correct geckodriver based on OS
        drivername = "/geckodriver.exe" if os.name == 'nt' else "/geckodriver"
        pathtodriver = os.path.dirname(os.path.realpath(__file__)) + drivername
        self.driver = webdriver.Firefox(executable_path=pathtodriver, desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)

        self.WEBSITE_URL = "http://localhost:8080/"


        # Different screenshot resolutions
        self.resolutions = [
            [1024, 768],
            [1280, 800],
            [1360, 768],
            [1366, 768],
            [1440, 900],
            [1600, 900],
            [1680, 1050],
            [1920, 1080],
            [360, 740],
            [480, 853],
            [414, 896],
            [768, 1024]
        ]

        if os.path.exists(f"screenshots"):
            shutil.rmtree("screenshots")

        if not os.path.exists(f"screenshots"):
            os.mkdir("screenshots")


    def takeScreenshots(self):
        driver = self.driver

        pages = ["index", "kontakt"]

        for page in pages:
            driver.get(self.WEBSITE_URL + page + ".html")

            if not os.path.exists(f"screenshots/{page}"):
                os.mkdir(f"screenshots/{page}")

            for resolution in self.resolutions:
                width = resolution[0]
                height = resolution[1]
                driver.set_window_size(width, height, driver.window_handles[0])
                driver.get_screenshot_as_file(f"{os.path.dirname(os.path.realpath(__file__))}/screenshots/{page}/screenshot-{width}x{height}.png")
                driver.get_full_page_screenshot_as_file(f"{os.path.dirname(os.path.realpath(__file__))}/screenshots/{page}/screenshot-{width}-full.png")

    def tearDown(self):
        self.driver.quit()

    # Runs the setup, takes screenshots then exits.
    def start(self):
        self.setUp()
        self.takeScreenshots()
        self.tearDown()


if __name__ == "__main__":
    sb = ScreenshotTest()
    sb.start()
