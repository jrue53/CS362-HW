import unittest
import average

class TestAverage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(average.averageList([1, 2, 3, 4, 5]), 3.0)

    def test_float(self):
        self.assertEqual(average.averageList([1.2, 3.5, 4.6, 5.7]), 3.75)
    
    def test_negative(self):
        self.assertEqual(average.averageList([-1, -2, -3, -4, -5]), -3.0)

    #failing tests
    def test_div_by_zero(self):
        self.assertEqual(average.averageList([]), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)