import unittest
import io
import sys
from operators import Operators, main

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

class MainTest(unittest.TestCase):
    def test_main_number_too_short(self):
        with self.assertRaises(Exception) as context:
            main(number="44444")

        self.assertTrue("Phone number too short!" in str(context.exception))

    def test_main_no_operator_found(self):
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput

        main(number="9876543210")

        sys.stdout = sys.__stdout__
        self.assertEqual("No operator found\n", capturedOutput.getvalue())

    def test_main_operator_with_best_price(self):
        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput

        main(number="462042600")

        sys.stdout = sys.__stdout__
        self.assertEqual(
            "Operator_A has the best price $0.0/min for number 462042600\n",
            capturedOutput.getvalue()
        )


if __name__ == '__main__':
    unittest.main()
