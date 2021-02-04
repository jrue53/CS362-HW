import unittest
import fullname

class TestFullname(unittest.TestCase):
    def test_normalname(self):
        self.assertEqual(fullname.full("Drew", "Turner"), "Drew Turner")
    
    def test_reverse_name(self):
        self.assertEqual(fullname.full("Werd", "Renrut"), "Werd Renrut")    

    def test_extraspace(self):
        self.assertEqual(fullname.full("Drew ", "Turner"), "Drew  Turner")

    #failing tests
    def test_types(self):
        self.assertEqual(fullname.full(1, 2), None)
        self.assertEqual(fullname.full(1.3, 2.5), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)