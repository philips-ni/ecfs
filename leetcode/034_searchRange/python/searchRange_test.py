
import unittest
import searchRange

class TestSearchrange(unittest.TestCase):
    def test_searchRange(self):
        s = searchRange.Solution()
        self.assertEqual(s.searchRange([1],1), [0,0])
        self.assertEqual(s.searchRange([1,2,3], 1), [0,0] )
        self.assertEqual(s.searchRange([1,1,1,2,3], 1), [0,2] )                                        
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3,4] )
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 100), [-1,-1] )
        self.assertEqual(s.searchRange([], 100), [-1,-1] )

if __name__ == '__main__':
    unittest.main()
