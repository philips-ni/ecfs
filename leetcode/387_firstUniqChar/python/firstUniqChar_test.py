
import unittest
import firstUniqChar

class TestFirstuniqchar(unittest.TestCase):
    def test_firstUniqChar(self):
        s = firstUniqChar.Solution()
        self.assertEqual(s.firstUniqChar("leetcode"), 0)
        self.assertEqual(s.firstUniqChar("loveleetcode"), 2)        
if __name__ == '__main__':
    unittest.main()
