
import unittest
import search_2d_matrix

class TestSearch_2D_Matrix(unittest.TestCase):
    def test_searchMatrix(self):
        s = search_2d_matrix.Solution()
        m1 = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertEqual(s.searchMatrix(m1, 23), True)
        self.assertEqual(s.searchMatrix(m1, 123), False)        
        m2  = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self.assertEqual(s.searchMatrix(m2, 3), True)
        self.assertEqual(s.searchMatrix(m2, 13), False)
        m3 = [[]]
        self.assertEqual(s.searchMatrix(m3, 1), False)        
if __name__ == '__main__':
    unittest.main()
