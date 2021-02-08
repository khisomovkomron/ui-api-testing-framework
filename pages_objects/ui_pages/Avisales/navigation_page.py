from base_helpers.ui_helpers.basepage import BasePage
import logging as logger

class NavigationPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = logger
        
    
    _hotels = "a[data-goal=hotelTab] "
    _business = "a[data-goal=businessTab] "
    _auto = "a[data-goal=carsTab] "
    _insurance = "a[data-goal=insuranceTab] "
    
    def navigate_to_hote_search(self):
        self.element_click(locator=self._hotels, locatortype="css")
    
    def navigate_to_business(self):
        self.element_click(locator=self._business, locatortype="css")
    
    def navigate_to_auto(self):
        element =self.wait_for_element(locator=self._auto, locatortype="css")
        self.element_click(element)
    
    def navigate_to_insurance(self):
        element = self.wait_for_element(locator=self._insurance, locatortype="css")
        self.element_click(locator=self._insurance, locatortype="css")
        
        w
    
    