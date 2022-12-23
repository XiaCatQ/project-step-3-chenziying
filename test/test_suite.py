import unittest
from Testing.test_Structure import test_User, test_calculation
from Testing.test_bankingUI import TestbankingUI
from Testing.test_bankingDS import TestbankingDS


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_User))
    suite.addTest(unittest.makeSuite(test_calculation))
    suite.addTest(unittest.makeSuite(TestbankingUI))
    suite.addTest(unittest.makeSuite(TestbankingDS))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

