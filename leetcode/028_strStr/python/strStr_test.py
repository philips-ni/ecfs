
import unittest
import strStr

class TestStrstr(unittest.TestCase):
    def test_strStr(self):
        s = strStr.Solution()
        self.assertEqual(s.strStr("mississippi","issippi"), 4 )                        
        self.assertEqual(s.strStr("mississippi","issipi"), -1 )
        self.assertEqual(s.strStr("hello","ll"),2 )
        self.assertEqual(s.strStr("zzzzzz","zz"),0 )        
        self.assertEqual(s.strStr("ll","hello"),-1 )
        self.assertEqual(s.strStr("ll","ll"), 0 )                
        self.assertEqual(s.strStr("aaaaa","bba"),-1 )
        self.assertEqual(s.strStr("",""), -1 )


if __name__ == '__main__':
    unittest.main()
