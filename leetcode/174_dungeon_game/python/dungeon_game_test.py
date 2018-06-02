import unittest
import dungeon_game

class TestDungeon_Game(unittest.TestCase):
    def test_calculateMinimumHP(self):
        s = dungeon_game.Solution()
        grid = [
            [-2,-3,3],
            [-5,-10,1],
            [10,30,-5]
            ]
        self.assertEqual(s.calculateMinimumHP(grid), 7)

        grid = [
            [1,-3,3],
            [0,-2,0],
            [-3,-3,-3]
            ]
        self.assertEqual(s.calculateMinimumHP(grid), 3)
        
if __name__ == '__main__':
    unittest.main()
