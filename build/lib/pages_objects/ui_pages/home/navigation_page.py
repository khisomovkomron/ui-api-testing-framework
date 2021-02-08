from base_helpers.ui_helpers.basepage import BasePage
import logging as logger


class NavigationPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logger

    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locatortype="link")

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locatortype="link")

    def navigate_to_practice(self):
        self.element_click(locator=self._practice, locatortype="link")

    def navigate_to_user_settings(self):
        user_setting_element = self.wait_for_element(locator=self._user_settings_icon,
                                                   locatortype="xpath")
        self.element_click(element=user_setting_element)
        self.element_click(locator=self._user_settings_icon, locatortype="xpath")


