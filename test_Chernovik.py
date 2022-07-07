import unittest
from Chernovik2 import Chernovik2
class Chernovik2(unittest.TestCase):
    def setUp(self):
        self.Chernovik2 = Chernovik2()
    def test_add(self):
        self.assertEqual(self.Chernovik2.add(7, 3), 10)
    def test_multiply(self):
        self.assertEqual(self.Chernovik2.multiply(7, 3), 21)
    def test_subtract(self):
        self.assertEqual(self.Chernovik2.subtract(7, 3), 4)
    def test_divide(self):
        self.assertEqual(self.Chernovik2.divide(21, 3), 7)    
if __name__ == "__main__":
    unittest.main()