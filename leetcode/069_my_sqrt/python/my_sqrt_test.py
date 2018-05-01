
import unittest
import my_sqrt

class TestMy_Sqrt(unittest.TestCase):
    def test_mySqrt(self):
        s = my_sqrt.Solution()
        self.assertEqual(s.mySqrt(91), 9 )
        self.assertEqual(s.mySqrt(1), 1 )        
        self.assertEqual(s.mySqrt(4), 2 )
        self.assertEqual(s.mySqrt(8), 2 )
        self.assertEqual(s.mySqrt(81), 9 )

        
if __name__ == '__main__':
    unittest.main()
