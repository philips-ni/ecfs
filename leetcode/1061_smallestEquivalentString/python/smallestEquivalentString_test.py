
import unittest
import smallestEquivalentString

class TestSmallestequivalentstring(unittest.TestCase):
    def test_smallestEquivalentString(self):
        s = smallestEquivalentString.Solution()
        self.assertEqual(s.smallestEquivalentString("parker", "morris", "parser"), "makkek")
        self.assertEqual(s.smallestEquivalentString("hello", "world","hold"), "hdld")
        self.assertEqual(s.smallestEquivalentString("leetcode", "programs","sourcecode"), "aauaaaaada")        
if __name__ == '__main__':
    unittest.main()
