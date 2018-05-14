
import unittest
import unique_paths2

class TestUnique_Paths2(unittest.TestCase):
    def test_uniquePathsWithObstacles(self):
        s = unique_paths2.Solution()
        i = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEqual(s.uniquePathsWithObstacles(i), 2)
        i = [
            [1]
        ]
        self.assertEqual(s.uniquePathsWithObstacles(i), 0)
        
if __name__ == '__main__':
    unittest.main()
