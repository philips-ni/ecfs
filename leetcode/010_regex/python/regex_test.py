import unittest
import regex

class TestRegex(unittest.TestCase):

    def test_isMatch(self):
        s = regex.Solution()
        self.assertEqual(False, s.isMatch("aabcde","c*a.*d"))        
        self.assertEqual(True, s.isMatch("aabcde","c*a.*de"))                
        self.assertEqual(True, s.isMatch("","c*c*"))
        self.assertEqual(True, s.isMatch("","c*"))        
        self.assertEqual(True, s.isMatch("a","ab*"))
        self.assertEqual(True, s.isMatch("ac","ab*c"))
        self.assertEqual(True, s.isMatch("ac","ab*c*c"))                
        
        self.assertEqual(False, s.isMatch("aabcde","c*a.*d"))
        self.assertEqual(False, s.isMatch("abcd","a.d"))        
        self.assertEqual(True, s.isMatch("aab","c*a*b"))                
        self.assertEqual(True, s.isMatch("aab","a*b"))        


        self.assertEqual(True, s.isMatch("aa","a*"))
        self.assertEqual(True, s.isMatch("",""))
        self.assertEqual(True, s.isMatch("","c*"))
        self.assertEqual(False, s.isMatch("aa","a"))
        self.assertEqual(True, s.isMatch("aa","aa"))
        self.assertEqual(False, s.isMatch("aaa","aa"))
        self.assertEqual(True, s.isMatch("aa",".*"))
        
        self.assertEqual(False, s.isMatch("abcd","d*"))
        self.assertEqual(False, s.isMatch("a",""))
        self.assertEqual(True, s.isMatch("aab","aab"))
        self.assertEqual(False, s.isMatch("aaaa","aaa"))
        self.assertEqual(False, s.isMatch("aaa","aaaaa"))        
        self.assertEqual(True, s.isMatch("abcd","abcd"))
        self.assertEqual(False, s.isMatch("aaaaaabbc","a*b*"))
        self.assertEqual(True, s.isMatch("abcd","a..d"))

        self.assertEqual(True, s.isMatch("aaaa","a*a"))
        # self.assertEqual(True, s.isMatch("a.*g","abcg"))



if __name__ == '__main__':
    unittest.main()
        
