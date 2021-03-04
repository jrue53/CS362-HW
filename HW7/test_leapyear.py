import unittest
import leapyear

class TestLeapYear(unittest.TestCase):
    def test_four(self):
        self.assertEqual(leapyear.ly(24), "This is a leap year")
        self.assertEqual(leapyear.ly(5), "This is not a leap year")

    def test_hundred(self):
        self.assertEqual(leapyear.ly(100), "This is a leap year")
        self.assertEqual(leapyear.ly(103), "This is not a leap year")


if __name__ == '__main__':
    unittest.main(verbosity=2)