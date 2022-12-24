import unittest 
from BankAccountSystem.Structure import User as U
from BankAccountSystem.Structure import calculation as cal

class test_calculation(unittest.TestCase): # test class
    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def setUpClass(cls):
        print('SetupClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def test_interest(self):
        self.assertEqual(round(cal.interest(1), 5), 0.0001)
        self.assertEqual(round(cal.interest(2), 5), 0.0002)
        self.assertEqual(round(cal.interest(3), 5), 0.0003)
        self.assertEqual(round(cal.interest(4), 5), 0.0004)

    def test_service(self):
        self.assertEqual(cal.service(100), 103)
        self.assertEqual(cal.service(200), 203)
        self.assertEqual(cal.service(300), 303)
        self.assertEqual(cal.service(400), 403)

unittest.main(argv=[''], verbosity=2, exit=False)