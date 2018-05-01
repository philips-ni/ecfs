import unittest
import longsubstr

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):
        s1 = "abcbacbb"
        s2 = "bbbbb"
        s3 = "pwwkew"
        s4 = "zzzzabcdefgabcd"
        s5 = "ywjvusw"
        s6 = "bziuwnklhqzrxnb"
        s7 = "feiyanxi"
        s8 = ""
        s9 = "xyzxyzzxydcz"
        s10 = "c"
        s11 = "ab"
        s12 = "aab"
        s = longsubstr.Solution()
        self.assertEqual(s.lengthOfLongestSubstring(s1), 3)
        self.assertEqual(s.lengthOfLongestSubstring(s2), 1)
        self.assertEqual(s.lengthOfLongestSubstring(s3), 3)
        self.assertEqual(s.lengthOfLongestSubstring(s4), 8)
        self.assertEqual(s.lengthOfLongestSubstring(s5), 6)
        self.assertEqual(s.lengthOfLongestSubstring(s6), 11)
        self.assertEqual(s.lengthOfLongestSubstring(s8), 0)
        self.assertEqual(s.lengthOfLongestSubstring(s9), 5)
        self.assertEqual(s.lengthOfLongestSubstring(s10), 1)
        self.assertEqual(s.lengthOfLongestSubstring(s11), 2)
        self.assertEqual(s.lengthOfLongestSubstring(s12), 2)

        
if __name__ == '__main__':
    unittest.main()
