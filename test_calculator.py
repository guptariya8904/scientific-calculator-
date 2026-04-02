import unittest
from basic_operations import add, divide
from advanced_operations import power

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_divide_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_complex_expression(self):
        sum_result = add(5, 5)
        final_result = power(sum_result, 2)
      
        self.assertEqual(final_result, 200)   # wrong on purpose

if __name__ == '__main__':
    unittest.main()