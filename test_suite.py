import unittest
import test_User
import test_calculation
import test_bankingUI
import test_bankingDS


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_User))
    suite.addTest(unittest.makeSuite(test_calculation))
    suite.addTest(unittest.makeSuite(test_bankingUI))
    suite.addTest(unittest.makeSuite(test_bankingDS))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

