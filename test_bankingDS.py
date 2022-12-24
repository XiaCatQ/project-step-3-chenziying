import unittest  # Jupyter notebook


from BankAccountSystem.Interface import bankingDS
import os

class test_bankingDS(unittest.TestCase): # test class
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

    def test_addAccount(self):
        self.assertEqual(bankingDS.addAccount('', 10001, 10, 200), "All fields required!")
        self.assertEqual(bankingDS.addAccount('Mary', '', 20, 200), 'All fields required!')
        self.assertEqual(bankingDS.addAccount('Tom', 10003, 30, 200), 'Account Already Exists!')
        self.assertEqual(bankingDS.addAccount('Jack', 10004, 50, 200), 'Account Already Exists!')


    def test_validate(self):
        self.assertEqual(bankingDS.validate('Mary', 999999), 'Please check your spell of name!')
        self.assertEqual(bankingDS.validate('Tom', 10003), True)
        self.assertEqual(bankingDS.validate('Jack', 10004), True)
        self.assertEqual(bankingDS.validate('Jaack', 10004), 'Please check your spell of name!')

unittest.main(argv=[''], verbosity=2, exit=False)

#%%
