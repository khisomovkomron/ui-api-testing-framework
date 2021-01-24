from selenium_ui.base.seleniumDriver import SeleniumDriver
from traceback import print_stack
from selenium_ui.utilities.util import Util
import logging as logger


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
        self.log = logger

    def verify_page_title(self, title_to_verify):

        try:
            actualtitle = self.get_title()
            return self.util.verifyTextContains(actualtitle, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False