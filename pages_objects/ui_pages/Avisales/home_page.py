from pages_objects.ui_pages.Avisales.navigation_page import NavigationPage
from base_helpers.ui_helpers.basepage import BasePage
import logging as logger

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.log = logger
        
    _origin = '#origin'
    _destination = '#destination'
    _departure_date = '.--departure.trip-duration__input-wrapper'
    _return_date = '.--return.trip-duration__input-wrapper'
    _select_departure_date = ''
    _select_arrival_date = ''
    
    def click_origin(self):
        self.element_click(locator=self._origin, locatortype='css')
        
    def enter_origin_city(self, city):
        self.send_keys(city, self._origin)
        
    def click_destination(self):
        self.element_click(locator=self._destination, locatortype='css')
        
    def enter_destination_city(self,city):
        self.send_keys(city, self._destination)
        
    