
import unittest
import divideTwoInt

class TestDividetwoint(unittest.TestCase):
    def test_divide(self):
        s = divideTwoInt.Solution()
        self.assertEqual(s.divide(4,2), 2)
        self.assertEqual(s.divide(100,51), 1)
        self.assertEqual(s.divide(1000,2000), 0)
        self.assertEqual(s.divide(1000,10), 100)
        self.assertEqual(s.divide(-10,5), -2)
        self.assertEqual(s.divide(0,1), 0)
        self.assertEqual(s.divide(-2147483648,-1), 2147483647)                
        
if __name__ == '__main__':
    unittest.main()
