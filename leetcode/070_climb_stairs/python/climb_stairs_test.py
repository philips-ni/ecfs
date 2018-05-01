
import unittest
import climb_stairs

class TestClimb_Stairs(unittest.TestCase):
    def test_climbStairs(self):
        s = climb_stairs.Solution()
        self.assertEqual(s.climbStairs(2),2 )
        self.assertEqual(s.climbStairs(3),3 )
        self.assertEqual(s.climbStairs(4),5 )
        self.assertEqual(s.climbStairs(5),8 )
        self.assertEqual(s.climbStairs(6),13 )
        self.assertEqual(s.climbStairs(35),14930352 )                                
if __name__ == '__main__':
    unittest.main()
