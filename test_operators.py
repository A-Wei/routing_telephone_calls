from operators import Operators
import unittest

class OperatorsTest(unittest.TestCase):
    def setUp(self):
        Operator_A = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '46732': 1.1,
        }

        Operator_B = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2,
        }
        ops = {
            'Operator_A': Operator_A,
            'Operator_B': Operator_B,
        }

    def tearDown(self):
        Operator_A.delete()
        Operator_B.delete()
        ops.delete()

    def test_find_prefix(self):
        prefixs = ["12345","1234","123","12","1"]
        phone_number = "12344321"

        prefix = Operators().find_prefix(phone_number, prefixs)

        self.assertEqual(prefix, "1234")

if __name__ == '__main__':
    unittest.main()
