import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_num(self):
        self.assertEqual(fizzbuzz.fb(), "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100")

    def test_fizz(self):
        self.assertEqual(fizzbuzz.fb(), "1, 2, fizz, 4, 5, fizz, 7, 8, fizz, 10, 11, fizz, 13, 14, fizz, 16, 17, fizz, 19, 20, fizz, 22, 23, fizz, 25, 26, fizz, 28, 29, fizz, 31, 32, fizz, 34, 35, fizz, 37, 38, fizz, 40, 41, fizz, 43, 44, fizz, 46, 47, fizz, 49, 50, fizz, 52, 53, fizz, 55, 56, fizz, 58, 59, fizz, 61, 62, fizz, 64, 65, fizz, 67, 68, fizz, 70, 71, fizz, 73, 74, fizz, 76, 77, fizz, 79, 80, fizz, 82, 83, fizz, 85, 86, fizz, 88, 89, fizz, 91, 92, fizz, 94, 95, fizz, 97, 98, fizz, 100"), 
if __name__ == '__main__':
    unittest.main(verbosity=2)