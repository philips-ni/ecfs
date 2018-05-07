
import unittest
import search_2d_matric

class TestSearch_2D_Matric(unittest.TestCase):
    def test_searchMatrix(self):
        s = search_2d_matric.Solution()
        m = []
        self.assertEqual(s.searchMatrix(m,15), False)
        
        m = [[]]
        self.assertEqual(s.searchMatrix(m,15), False)
        
        m = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]]
        self.assertEqual(s.searchMatrix(m,15), True)
        
        m = [
            [-1],
            [-1]
        ]
        self.assertEqual(s.searchMatrix(m,-2), False)
        self.assertEqual(s.searchMatrix(m,20), False)        
        
        m = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertEqual(s.searchMatrix(m,5), True)
        self.assertEqual(s.searchMatrix(m,20), False)
        self.assertEqual(s.searchMatrix(m,200), False)        
        m = [[]]
        self.assertEqual(s.searchMatrix(m,5), False)
        self.assertEqual(s.searchMatrix(m,20), False)        
        m = [[1,5,20]]
        self.assertEqual(s.searchMatrix(m,5), True)
        self.assertEqual(s.searchMatrix(m,20), True)        
        m = [[5]]
        self.assertEqual(s.searchMatrix(m,5), True)
        self.assertEqual(s.searchMatrix(m,20), False)

        
        
        
if __name__ == '__main__':
    unittest.main()
