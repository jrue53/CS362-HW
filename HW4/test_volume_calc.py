import unittest
import volume_calc

class TestVolume(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(volume_calc.volume(3), 27)
   
    def test_negative(self):
        self.assertEqual(volume_calc.volume(-3), -27)

    #failing tests
    def test_types(self):
        self.assertEqual(volume_calc.volume("string"), None)
        self.assertEqual(volume_calc.volume(True), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)