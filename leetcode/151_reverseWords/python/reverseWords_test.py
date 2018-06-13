
import unittest
import reverseWords

class TestReversewords(unittest.TestCase):
    def test_reverseWords(self):
        s = reverseWords.Solution()
        self.assertEqual(s.reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(s.reverseWords("   abc def"), "def abc")
        self.assertEqual(s.reverseWords("   abc"), "abc")
        self.assertEqual(s.reverseWords("abc"), "abc")
        self.assertEqual(s.reverseWords("abc   "), "abc")        
if __name__ == '__main__':
    unittest.main()
