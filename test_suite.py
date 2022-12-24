import unittest
from test_User import *
from test_calculation import *
from test_bankingUI import *
from test_bankingDS import *


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_User))
    suite.addTest(unittest.makeSuite(test_calculation))
    suite.addTest(unittest.makeSuite( test_bankingUI))
    suite.addTest(unittest.makeSuite(test_bankingDS))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

