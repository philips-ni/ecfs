
import unittest
import zuma_game

class TestZuma_Game(unittest.TestCase):
    def test_findMinStep(self):
        s = zuma_game.Solution()
        self.assertEqual(s.findMinStep("WRRBBW","RB"), -1)
        self.assertEqual(s.findMinStep("WWRRBBWW","WRBRW"), 2)        
if __name__ == '__main__':
    unittest.main()
