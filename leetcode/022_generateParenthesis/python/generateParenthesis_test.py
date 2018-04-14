
import unittest
import generateParenthesis

class TestGenerateparenthesis(unittest.TestCase):
    def test_generateParenthesis(self):
        s = generateParenthesis.Solution()
        self.assertEqual(s.generateParenthesis(0), [])
        self.assertEqual(s.generateParenthesis(1), ["()"])
        self.assertEqual(s.generateParenthesis(2), ["(())","()()"])
        self.assertEqual(s.generateParenthesis(3), ["((()))","(()())","(())()", "()(())","()()()"])  
if __name__ == '__main__':
    unittest.main()
