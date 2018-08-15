
import unittest
import best_meeting_point

class TestBest_Meeting_Point(unittest.TestCase):
    def test_minTotalDistance(self):
        s = best_meeting_point.Solution()
        grid = [
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]
        ]
        self.assertEqual(s.minTotalDistance(grid), 6)
        grid = [
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(s.minTotalDistance(grid), 4)

        grid = [
            [0,0,0,0,1],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(s.minTotalDistance(grid), 0)

        grid = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(s.minTotalDistance(grid), -1)
        
if __name__ == '__main__':
    unittest.main()
