
import unittest
import Ternary_Expression_Parser

class TestTernary_Expression_Parser(unittest.TestCase):
    def test_parseTernary(self):
        s = Ternary_Expression_Parser.Solution()
        self.assertEqual(s.parseTernary("T?2:3"),'2')
        self.assertEqual(s.parseTernary("F?1:T?4:5"),'4')
        self.assertEqual(s.parseTernary("T?T?F:5:3"),'F')                
if __name__ == '__main__':
    unittest.main()
