import unittest
from tests_ui_api.ui_tests.test_login import TestLogin


tc1 =unittest.TestLoader().loadTestsFromTestCase(TestLogin)

smokeTest =unittest.TestSuite[tc1]

unittest.TextTestRunner(verbosity=2).run(smokeTest)