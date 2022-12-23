import unittest 
import sys
sys.path.append('C:\\Users\\sophiechen\\2022MDS\\Block 3\\Data-533\\project\\step2\\DATA533-testing\\')
from BankAccountSystem.Structure import User as U
from BankAccountSystem.Structure import calculation as cal

class test_User(unittest.TestCase): # test class 

    def setUp(self):
        self.user1 = U.User('Sherry', 10000)
        self.user2 = U.User('Yuki', 11111)
        self.user3 = U.User('Nyx', 22222)
        self.user4 = U.User('Shveta', 33333)
        self.newuser1 = U.newUser('Sherry', 10000, 10)
        self.newuser2 = U.newUser('Yuki', 11111, 20)
        self.newuser3 = U.newUser('Nyx', 22222, 30)
        self.newuser4 = U.newUser('Shveta', 33333, 40)


    def test_user(self):
        self.assertIsInstance(self.user1 , U.User)
        self.assertIsInstance(self.user2 , U.User)
        self.assertIsInstance(self.user3 , U.User)
        self.assertIsInstance(self.user4 , U.User)

    def test_newUser(self):
        self.assertIsInstance(self.newuser1 , U.newUser)
        self.assertIsInstance(self.newuser2 , U.newUser)
        self.assertIsInstance(self.newuser3 , U.newUser)
        self.assertIsInstance(self.newuser4 , U.newUser)

unittest.main(argv=[''], verbosity=2, exit=False)


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