import unittest
import countAndSay

class TestCountandsay(unittest.TestCase):
    def test_countAndSay(self):
        s = countAndSay.Solution()
        self.assertEqual(s.countAndSay(1), "1")
        self.assertEqual(s.countAndSay(2), "11")
        self.assertEqual(s.countAndSay(3), "21")
        self.assertEqual(s.countAndSay(4), "1211")
        self.assertEqual(s.countAndSay(5), "111221")                                
if __name__ == '__main__':
    unittest.main()
