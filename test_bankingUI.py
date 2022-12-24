import unittest  # Jupyter notebook


from BankAccountSystem.Interface import bankingDS as ds
from BankAccountSystem.Interface import bankingUI



class test_bankingUI(unittest.TestCase):  # test class
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
        self.assertEqual(bankingUI.signup(), None)
        self.assertEqual(bankingUI.signup(),  None)
        self.assertEqual(bankingUI.signup(), None)
        self.assertEqual(bankingUI.signup(), None)

    def test_withdraw(self):
        self.assertEqual(bankingUI.withdraw(),  None)
        self.assertEqual(bankingUI.withdraw(), None )
        self.assertEqual(bankingUI.withdraw(),  None)
        self.assertEqual(bankingUI.withdraw(),  None)



unittest.main(argv=[''], verbosity=2, exit=False)


#%%
