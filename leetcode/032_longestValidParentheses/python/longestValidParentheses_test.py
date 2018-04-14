
import unittest
import longestValidParentheses

class TestLongestvalidparentheses(unittest.TestCase):
    def test_longestValidParentheses(self):
        s = longestValidParentheses.Solution()
        self.assertEqual(s.longestValidParentheses(")(())))(())())"), 6)                
        self.assertEqual(s.longestValidParentheses("(()"), 2)
        self.assertEqual(s.longestValidParentheses(")()())"), 4)

        
if __name__ == '__main__':
    unittest.main()
