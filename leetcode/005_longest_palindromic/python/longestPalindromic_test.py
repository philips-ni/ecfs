import unittest
import longestPalindromic

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_longestPalindrome(self):
        s = longestPalindromic.Solution()
        s1 = "babad"
        s2 = "cbbd"
        s3 = "b"
        s4 = ""
        s5 = "bac"
        s6 = "aaaa"
        s7 = "aaaabbb"
        s8 = "aaabaaaa"
        s9 = "abacdfgdcaba"
        s10 = """zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"""
        self.assertEqual("bab", s.longestPalindrome(s1))
        self.assertEqual("bb", s.longestPalindrome(s2))
        self.assertEqual("b", s.longestPalindrome(s3))
        self.assertEqual("", s.longestPalindrome(s4))
        self.assertEqual("b", s.longestPalindrome(s5))
        self.assertEqual("aaaa", s.longestPalindrome(s6))
        self.assertEqual("aaaa", s.longestPalindrome(s7))
        self.assertEqual("aaabaaa", s.longestPalindrome(s8))
        self.assertEqual("aba", s.longestPalindrome(s9))
        self.assertEqual(s10, s.longestPalindrome(s10))

        
if __name__ == '__main__':
    unittest.main()
