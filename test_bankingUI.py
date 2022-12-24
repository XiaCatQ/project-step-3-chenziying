import unittest  # Jupyter notebook


from BankAccountSystem.Interface import bankingDS as ds
from BankAccountSystem.Interface import bankingUI



class TestbankingUI(unittest.TestCase):  # test class
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

    def test_signup(self):
        self.assertEqual(bankingUI.signup('John', 10001, 10), 'John')
        self.assertEqual(bankingUI.signup('Mary', 10002, 20), 'Mary')
        self.assertEqual(bankingUI.signup('Tom', 10003, 30), 'Tom')
        self.assertEqual(bankingUI.signup('Jack', 10004, 50), 'Jack')

    def test_withdraw(self):
        self.assertEqual(bankingUI.withdraw('withdraw'), 'withdraw')
        self.assertEqual(bankingUI.withdraw('deposit'), 'withdraw')
        self.assertEqual(bankingUI.withdraw('22'), 'withdraw')
        self.assertEqual(bankingUI.withdraw('depo'), 'with')



unittest.main(argv=[''], verbosity=2, exit=False)


#%%
