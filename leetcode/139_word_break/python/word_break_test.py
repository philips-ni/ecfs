
import unittest
import word_break

class TestWord_Break(unittest.TestCase):
    def test_wordBreak(self):
        s = word_break.Solution()
        self.assertEqual(s.wordBreak("leetcode", ["leet", "code"]),True )
        self.assertEqual(s.wordBreak("applepenapple", ["apple", "pen"]),True )
        self.assertEqual(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]),False )
        txt = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict =["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        self.assertEqual(s.wordBreak(txt,wordDict), False)
        
if __name__ == '__main__':
    unittest.main()
