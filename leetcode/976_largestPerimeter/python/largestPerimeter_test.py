
import unittest
import largestPerimeter

class TestLargestperimeter(unittest.TestCase):
    def test_largestPerimeter(self):
        s = largestPerimeter.Solution()
        self.assertEqual(s.largestPerimeter([2,1,2]), 5)
        self.assertEqual(s.largestPerimeter([1,2,1]), 0)
        self.assertEqual(s.largestPerimeter([3,2,3,4]), 10)
        self.assertEqual(s.largestPerimeter([3,6,2,3]), 8)        
if __name__ == '__main__':
    unittest.main()
