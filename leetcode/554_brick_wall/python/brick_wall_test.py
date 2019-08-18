
import unittest
import brick_wall

class TestBrick_Wall(unittest.TestCase):
    def test_leastBricks(self):
        s = brick_wall.Solution()
        wall = [[1,2,2,1],
                [3,1,2],
                [1,3,2],
                [2,4],
                [3,1,2],
                [1,3,1,1]]
        
        self.assertEqual(s.leastBricks(wall), 2)
        wall = [[1,2],[2,1]]
        self.assertEqual(s.leastBricks(wall), 1)                
        wall = [[1,2],[2,1],[1,2]]
        self.assertEqual(s.leastBricks(wall), 1)
        wall = [[1,2]]
        self.assertEqual(s.leastBricks(wall), 0)
        wall = [[1,2],[2,1],[1,2]]
        self.assertEqual(s.leastBricks(wall), 1)
        wall = [[1],[1],[1]]
        self.assertEqual(s.leastBricks(wall), 3)
        wall = [[6, 2, 2], [1, 4, 4, 1], [2, 5, 3]]
        self.assertEqual(s.leastBricks(wall), 2)
        wall = [[79, 12, 208, 1]]
        self.assertEqual(s.leastBricks(wall), 0)
        wall = [[1]]
        self.assertEqual(s.leastBricks(wall), 1)        
        
if __name__ == '__main__':
    unittest.main()
