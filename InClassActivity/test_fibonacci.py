import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(fibonacci.fib(-3), None)
        
    def test_zero_one(self):
        self.assertEqual(fibonacci.fib(0), 0)
        self.assertEqual(fibonacci.fib(1), 1)

    def test_n(self):
        self.assertEqual(fibonacci.fib(5), 5)
        self.assertEqual(fibonacci.fib(4), 3)
        self.assertEqual(fibonacci.fib(15), 610)

    def test_n_fac(self):
        self.assertEqual(fibonacci.factorial(3), 6)
        self.assertEqual(fibonacci.factorial(5), 120)
        self.assertEqual(fibonacci.factorial(4), 24)

    def test_neg_fac(self):
        self.assertEqual(fibonacci.factorial(-3), None)

    def test_zero_one_fac(self):
        self.assertEqual(fibonacci.factorial(0), 1)
        self.assertEqual(fibonacci.factorial(1), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)