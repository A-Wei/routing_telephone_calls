from operators import Operators
import unittest

class OperatorsTest(unittest.TestCase):
    def test_best_operator_and_price_return_operator_a(self):
        phone_number = 12344321

        operator, best_price = Operators(phone_number).best_operator_and_price()

        self.assertEqual(operator, "Operator_A")
        self.assertEqual(best_price, 0.9)

    def test_best_operator_and_price_return_operator_b(self):
        phone_number = 44344321

        operator, best_price = Operators(phone_number).best_operator_and_price()

        self.assertEqual(operator, "Operator_B")
        self.assertEqual(best_price, 0.5)

    def test_best_operator_and_price_return_none(self):
        phone_number = 812344321

        operator, best_price = Operators(phone_number).best_operator_and_price()

        self.assertEqual(operator, None)
        self.assertEqual(best_price, None)


if __name__ == '__main__':
    unittest.main()
