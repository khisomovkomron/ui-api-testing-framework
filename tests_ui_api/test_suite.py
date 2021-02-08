import unittest
from tests_ui_api.ui_tests.test_login import TestLogin
from HtmlTestRunner import HTMLTestRunner
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin) #smoke test for example
tc2 =unittest.TestLoader().loadTestsFromTestCase(TestSignup) #functional test for example
# tc3 =unittest.TestLoader().loadTestsFromTestCase(TestHome) #smoke test for example

smokeTest = unittest.TestSuite([tc1])
functionalTest =unittest.TestSuite([tc2])
smokeTest =unittest.TestSuite([tc3])
regressionTest =unittest.TestSuite([tc1, tc2, tc3])



unittest.TextTestRunner(verbosity=2).run(smokeTest)
# unittest.TextTestRunner(verbosity=2).run(regressionTest)


outfile = open("C:/Users/komro/PycharmProjects/ui_api_testing_framework/Report.html", "w")
runner = HTMLTestRunner(
                combine_reports=True,
                verbosity=2
                )

runner.run(tc1)
runner.run(tc2)
runner.run(tc3)
runner.run(tc4)