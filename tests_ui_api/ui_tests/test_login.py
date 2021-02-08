import unittest
import pytest
from pages_objects.ui_pages.home.login_page import LoginPage
from base_helpers.ui_helpers.status import Status

pytestmark = [pytest.mark.ui, pytest.mark.smoke, pytest.mark.regression]


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.ui
    def test_t22validLogin(self, classSetup):
        self.lp.login("test1@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "title verification")
        result2 = self.lp.verify_login_successful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.mark_final("test_t2validLogin", result2, "login verification")

    @pytest.mark.ui
    def test_t22validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "title verification")
        result2 = self.lp.verify_login_successful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.mark_final("test_t2validLogin", result2, "login verification")
