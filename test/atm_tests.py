import unittest
from src.atm import ATM, InvalidPinException, InsufficientFundsException

class ATMTestCase(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()

    def test_check_balance_valid_pin(self):
        self.assertEqual(self.atm.check_balance(1234), 1500.0)
        self.assertEqual(self.atm.check_balance(0), 500.0)  # PIN 0000 jako 0
        self.assertEqual(self.atm.check_balance(4321), 3000.0)

    def test_check_balance_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(9999)

    def test_deposit_valid(self):
        self.assertEqual(self.atm.deposit(1234, 200), 1700.0)
        self.assertEqual(self.atm.check_balance(1234), 1700.0)

    def test_deposit_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(9999, 100)

    def test_deposit_non_positive_amount(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, 0)
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -100)

    # Testy metody withdraw
    def test_withdraw_valid(self):
        self.assertEqual(self.atm.withdraw(1234, 300), 1200.0)
        self.assertEqual(self.atm.check_balance(1234), 1200.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(0, 600)

    def test_withdraw_invalid_pin(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(9999, 100)

    def test_withdraw_non_positive_amount(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, 0)
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -100)


if __name__ == '__main__':
    unittest.main()
