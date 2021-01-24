from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging as logger
import time
import os
from traceback import print_stack


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver
        self.log = logger

    def screenshot(self, resultmessage):
        file_name = resultmessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relativer_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relativer_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.mkdir(destination_directory)
            self.driver.save_screenshots(destination_file)
        except:
            self.log.info("$$$ Exception occurred when taking screenshots")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        if locatortype == "name":
            return By.NAME
        if locatortype == "xpath":
            return By.XPATH
        if locatortype == "css":
            return By.CSS_SELECTOR
        if locatortype == "class":
            return By.CLASS_NAME
        if locatortype == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatortype + " not correct/supported")
        return False

    def get_element(self, locator, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            bytype = self.get_by_type(locatortype)
            element = self.driver.find_element(bytype, locator)
            self.log.info("Element found with locator:" + locator +
                          " and locatorType:" + locatortype)
        except:
            self.log.info("Element not found with locator:" + locator +
                          " and locatorType:" + locatortype)
        return element

    def get_element_list(self, locator, locatortype="id"):

        element = None

        try:
            locatortype = locatortype.lower()
            bytype = self.get_by_type(locatortype)
            element = self.driver.find_element(bytype, locatortype)
            self.log.info("Element found with locator:" + locator + " and locatorType:" + locatortype)
        except:
            self.log.info("Element not found with locator:" + locator + " and locatorType:" + locatortype)
        return element

    def element_click(self, locator="", locatortype="", element=None):

        try:
            if locator:
                element = self.get_element(locator, locatortype)
            element.click()
            self.log.info("Clicked on element with locator:" + locator +
                          "locatorType:" + locatortype)
        except:
            self.log.info("Cannot clicked on the element with locator" + locator +
                          " locatorType:" + locatortype)
            print_stack()

    def send_keys(self, data, locator="", locatortype="", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator:" + locator +
                          " locatorType:" + locatortype)
        except:
            self.log.info("Cannot send data on element with locator:" + locator +
                          " locatorType:" + locatortype)
            print_stack()

    def clear_field(self, locator="", locatortype=""):
        element = self.get_element(locator, locatortype)
        element.clear()
        self.log.info("Clear field with locator:" + locator +
                      " locatorType:" + locatortype)

    def get_text(self, locator="", locatortype="", element=None, info=""):
        try:
            if locator:
                element = self.get_element(locator, locatortype)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element::" + info)
                self.log.info("The test is :: " + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element" + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locatortype="", element=None):
        try:
            if locator:
                element = self.get_element(locator, locatortype)
            if element is not None:
                self.log.info("Element present with locator" + locator +
                              " locatorType" + locatortype)
                return True
            else:
                self.log.info("Element not present with locator" + locator +
                              " locatorType:" + locatortype)
                return False
        except:
            print("element not found")
            return False

    def is_element_displayed(self, locator="", locatortype="id", element=None):
        isdisplayed = False

        try:
            if locator:
                element = self.get_element(locator, locatortype)
            if element is not None:
                isdisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isdisplayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, bytype):
        try:
            elementlist = self.driver.find_element(bytype, locator)
            if len(elementlist) > 0:
                self.log.info("Element present with locator:" + locator
                              + " locatorType" + str(bytype))
                return True
            else:
                self.log.info("Element not present with locator:" + locator +
                              " locatorType: " + str(bytype))
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locatortype="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            bytype = self.get_by_type(locatortype)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((bytype, locatortype)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction="up"):

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
