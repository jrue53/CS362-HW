import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.calculator_add(3.2, 3.3), 6.5)
        self.assertEqual(calculator.calculator_add("abs", "jhs"), None)
        self.assertEqual(calculator.calculator_add(True, False), None)
   
    def test_subtraction(self):
        self.assertEqual(calculator.calculator_sub(3.5, 1.0), 2.5)
        self.assertEqual(calculator.calculator_sub(1.0, 3.5), -2.5)
        self.assertEqual(calculator.calculator_sub("abs", "jhs"), None)
        self.assertEqual(calculator.calculator_sub(True, False), None)

    def test_multiplication(self):
        self.assertEqual(calculator.calculator_mul(3.5, 3.5), 12.25)
        self.assertEqual(calculator.calculator_mul("abs", "jhs"), None)
        self.assertEqual(calculator.calculator_mul(True, False), None)

    def test_division(self):
        self.assertEqual(calculator.calculator_div(9.0, 4.0), 2.25)
        self.assertEqual(calculator.calculator_div(9.0, 0.0), None)
        self.assertEqual(calculator.calculator_div("abs", "jhs"), None)
        self.assertEqual(calculator.calculator_div(True, False), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)