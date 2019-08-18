
import unittest
import removeKdigits

class TestRemovekdigits(unittest.TestCase):
    def test_removeKdigits(self):
        s = removeKdigits.Solution()
        self.assertEqual(s.removeKdigits("1432219", 3), "1219")
        self.assertEqual(s.removeKdigits("10200", 1), "200")
        self.assertEqual(s.removeKdigits("10", 2), "0")
        self.assertEqual(s.removeKdigits("9", 1), "0")
        self.assertEqual(s.removeKdigits("91", 1), "1")
        self.assertEqual(s.removeKdigits("112", 1), "11")
        # self.assertEqual(s.removeKdigits("112", 2), "1")                                        
if __name__ == '__main__':
    unittest.main()
