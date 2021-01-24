import unittest
import pytest
from selenium_ui.pages.home.login_page import LoginPage
from selenium_ui.utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t22validLogin(self):
        self.lp.login("test1@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "title verification")
        result2 = self.lp.verify_login_successful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.mark_final("test_t2validLogin", result2, "login verification")

    @pytest.mark.run(order=2)
    def test_t22validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "title verification")
        result2 = self.lp.verify_login_successful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.mark_final("test_t2validLogin", result2, "login verification")