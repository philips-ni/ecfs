
import unittest
import longestSubstring

class TestLongestsubstring(unittest.TestCase):
    def test_longestSubstring(self):
        s = longestSubstring.Solution()
        self.assertEqual(s.longestSubstring("aaabb", 3), 3)
        self.assertEqual(s.longestSubstring("ababbc", 2), 5)
        self.assertEqual(s.longestSubstring("aaabbbdcccdc", 3), 6)                
if __name__ == '__main__':
    unittest.main()
