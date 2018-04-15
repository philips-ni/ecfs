
import unittest
import myPow

class TestMypow(unittest.TestCase):
    def test_myPow(self):
        s = myPow.Solution()
        self.assertEqual(s.myPow(2,-2),0.25 )        
        self.assertEqual(s.myPow(2,2),4 )
        self.assertEqual(s.myPow(2,0), 1)
        self.assertEqual(s.myPow(2,1), 2)
        self.assertEqual(s.myPow(2,3), 8)        
        
if __name__ == '__main__':
    unittest.main()
