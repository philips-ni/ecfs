import unittest
import longestCommonPrefix

class TestLongestcommonprefix(unittest.TestCase):
    def test_longestCommonPrefix(self):
        s = longestCommonPrefix.Solution()
        self.assertEqual("", s.longestCommonPrefix(["",""]))
        self.assertEqual("", s.longestCommonPrefix(["a","",""]))
        self.assertEqual("ab", s.longestCommonPrefix(["ab","abc","abcd"]) )
        self.assertEqual("", s.longestCommonPrefix(["a","b","c","a"]) )
        self.assertEqual("abcd", s.longestCommonPrefix(["abcd"]))
        self.assertEqual("abcd", s.longestCommonPrefix(["abcd","abcd","abcd"]))
        self.assertEqual("abcd", s.longestCommonPrefix(["abcdeeee","abcd","abcd","abcdeeee"]))
        
if __name__ == '__main__':
    unittest.main()
