from selenium_ui.base.basepage import BasePage
import logging as logger
from selenium_ui.pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.log = logger

    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user password"
    _login_button = "commit"

    def click_login_link(self):
        self.element_click(self._login_link, locatortype="link")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locatortype="name")

    def login(self, email="", password=""):
        self.click_login_link()
        self.clear_field()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        self.wait_for_element("                ")
        result = self.is_element_present(locator="//div[@id='navbar']//li[@class='dropdown']"
                                         , locatortype="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(locator="//div[contains(text(),'Invalid email or password')]",
                                         locatortype="xpath")
        return result

    def verify_login_title(self):
        return self.verify_page_title("Let's Kode it")

    def clear_fields(self):
        emailField = self.get_element(locator=self._email_field)
        emailField.clear()
        passwordField = self.get_element(locator=self._password_field)
        passwordField.clear()

    def logout(self):
        self.nav.navigate_to_user_settings()
        logoutLinkElement= self.wait_for_element(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                 locatortype="xpath", pollFrequency=1)
        self.element_click(element=logoutLinkElement)
        self.element_click(locator="//div[@id='navbar']//a[@href='/sign_out']",
                           locatortype="xpath")

