
import unittest
import groupAnagrams

class TestGroupanagrams(unittest.TestCase):
    def test_groupAnagrams(self):
        s = groupAnagrams.Solution()
        l1 =  ["eat", "tea", "tan", "ate", "nat", "bat"]
        ret = s.groupAnagrams(l1)
        print ret
        # self.assertEqual(s.groupAnagrams(), )

    def test_getSign(self):
        s = groupAnagrams.Solution()
        self.assertEqual(s.getSign("abc"), "a1,b1,c1,")
        self.assertEqual(s.getSign("cba"), "a1,b1,c1,")
        self.assertEqual(s.getSign("cbaa"), "a2,b1,c1,")        
if __name__ == '__main__':
    unittest.main()
