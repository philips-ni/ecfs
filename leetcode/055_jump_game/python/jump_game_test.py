
import unittest
import jump_game

class TestJump_Game(unittest.TestCase):
    def test_canJump(self):
        s = jump_game.Solution()
        self.assertEqual(s.canJump([1,2,0,1]), True)        
        self.assertEqual(s.canJump([2,3,1,1,4]), True)
        self.assertEqual(s.canJump([3,2,1,0,4]), False)
        self.assertEqual(s.canJump([0]), True)
        self.assertEqual(s.canJump([0,0]), False)
        self.assertEqual(s.canJump([0]), True)
        self.assertEqual(s.canJump([0,1]), False)
        self.assertEqual(s.canJump([1,0,2,1]), False)
        self.assertEqual(s.canJump([2,0,0,1]), False)
        self.assertEqual(s.canJump([2,0,1,0]), True)                        
        
        
if __name__ == '__main__':
    unittest.main()
