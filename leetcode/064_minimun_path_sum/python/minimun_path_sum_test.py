
import unittest
import minimun_path_sum

class TestMinimun_Path_Sum(unittest.TestCase):
    def test_minPathSum(self):
        s = minimun_path_sum.Solution()
        grid = [
            [1,3,1,4],
            [1,5,1,7],
            [4,2,1,3]
        ]
        self.assertEqual(s.minPathSum(grid), 10)
        
"""        
        grid = [
            [1,3,1],
            [1,1,1],
            [4,0,1]
        ]
        self.assertEqual(s.minPathSum(grid), 4)
        grid = [
            [1],
        ]
        self.assertEqual(s.minPathSum(grid), 1)
"""
        
if __name__ == '__main__':
    unittest.main()
