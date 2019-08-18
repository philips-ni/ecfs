
import unittest
import intersectionOf2ArrayII

class TestIntersectionof2Arrayii(unittest.TestCase):
    def test_intersection(self):
        s = intersectionOf2ArrayII.Solution()
        self.assertEqual(s.intersection([1,2,2,1],[2,2]),[2,2])
        self.assertEqual(sorted(s.intersection([4,9,5],[9,4,9,8,4])),[4,9])
        self.assertEqual(s.intersection([1,2,2,1,1],[1,2,2,2]),[1,2,2])        
if __name__ == '__main__':
    unittest.main()
