import cal_code
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = cal_code.add(2, 5)
        self.assertEqual(result, 7)
        
    def test_subtraction(self):
        result = cal_code.subtract(4,2)
        self.assertEqual(result, 2)
        
        
if __name__ == '__main__':
    unittest.main()
