
import unittest
import factorial_trailing_zeroes

class TestFactorial_Trailing_Zeroes(unittest.TestCase):
    def test_trailingZeroes(self):
        s = factorial_trailing_zeroes.Solution()
        self.assertEqual(s.trailingZeroes(3),0 )
        self.assertEqual(s.trailingZeroes(5),1 )

        s = factorial_trailing_zeroes.Solution1()
        self.assertEqual(s.trailingZeroes(3),0 )
        self.assertEqual(s.trailingZeroes(5),1 )        
        
if __name__ == '__main__':
    unittest.main()
