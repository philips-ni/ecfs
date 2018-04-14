
import unittest
import validParentheses

class TestValidparentheses(unittest.TestCase):
    def test_isValid(self):
        s = validParentheses.Solution()
        self.assertEqual(s.isValid(""), True)                        
        self.assertEqual(s.isValid("["), False)
        self.assertEqual(s.isValid(")"), False)                
        self.assertEqual(s.isValid("()[]{}"), True)
        self.assertEqual(s.isValid("([]){}"), True)
        self.assertEqual(s.isValid("([]){([{}])}"), True)        
        self.assertEqual(s.isValid("([(]){}"), False)
if __name__ == '__main__':
    unittest.main()
