
import unittest
import intersectionOf2Array

class TestIntersectionof2Array(unittest.TestCase):
    def test_intersection(self):
        s = intersectionOf2Array.Solution()
        self.assertEqual(s.intersection([1,2,2,1],[2,2]),[2])
        self.assertEqual(s.intersection([4,9,5],[9,4,9,8,4]),[9,4])        
if __name__ == '__main__':
    unittest.main()
