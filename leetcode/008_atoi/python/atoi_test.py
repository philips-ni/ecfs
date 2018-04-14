import unittest
import atoi

class TestAtoi(unittest.TestCase):

    def test_myAtoi(self):
        s = atoi.Solution()
        self.assertEqual(1,s.myAtoi("1"))
        self.assertEqual(321,s.myAtoi("321"))
        self.assertEqual(321,s.myAtoi("   321"))
        self.assertEqual(321,s.myAtoi("   321abc"))
        self.assertEqual(0,s.myAtoi(""))
        self.assertEqual(0,s.myAtoi("   +"))
        self.assertEqual(1,s.myAtoi("   +1"))
        self.assertEqual(0,s.myAtoi("-"))
        self.assertEqual(0,s.myAtoi("afafasdf"))
        self.assertEqual(0,s.myAtoi("afafasdf0"))
        self.assertEqual(0,s.myAtoi("afafasdf0"))
        self.assertEqual(0,s.myAtoi("afafasdf9.1"))
        self.assertEqual(123,s.myAtoi("  +123"))
        self.assertEqual(123,s.myAtoi("+123"))
        self.assertEqual(-123,s.myAtoi("-123"))
        self.assertEqual(-123,s.myAtoi("  -123"))
        
    def test_findStartIdx(self):
        s = atoi.Solution()
        self.assertEqual(0,s.findStartIdx("1"))

if __name__ == '__main__':
    unittest.main()
        
