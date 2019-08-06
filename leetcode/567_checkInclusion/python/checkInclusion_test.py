
import unittest
import checkInclusion

class TestCheckinclusion(unittest.TestCase):
    def test_checkInclusion(self):
        s = checkInclusion.Solution()
        self.assertEqual(s.checkInclusion("ab","eidbaooo"), True)
        self.assertEqual(s.checkInclusion("ab","eidboaooo"), False)
        self.assertEqual(s.checkInclusion("a","ab"), True)                        
        self.assertEqual(s.checkInclusion("ab","ab"), True)
        self.assertEqual(s.checkInclusion("ab","bcaab"), True)
        self.assertEqual(s.checkInclusion("kitten","sitting"), False)        
if __name__ == '__main__':
    unittest.main()
