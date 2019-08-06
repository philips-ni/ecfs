
import unittest
import removeOuterParentheses

class TestRemoveouterparentheses(unittest.TestCase):
    def test_removeOuterParentheses(self):
        s = removeOuterParentheses.Solution()
        self.assertEqual(s.removeOuterParentheses("(()())(())"), "()()()")
        self.assertEqual(s.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")
        self.assertEqual(s.removeOuterParentheses("()()"), "")
        
if __name__ == '__main__':
    unittest.main()
