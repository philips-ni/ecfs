import unittest
import target_sum

class TestTarget_Sum(unittest.TestCase):
    def test_findTargetSumWays(self):
        s = target_sum.Solution()
        self.assertEqual(s.findTargetSumWays([1, 1, 1, 1, 1], 3), 5 )
        self.assertEqual(s.findTargetSumWays([0,0],0), 4)                
        self.assertEqual(s.findTargetSumWays([0,0,0,0,0,0,0,0],0), 256)        
        self.assertEqual(s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1), 256)
        self.assertEqual(s.findTargetSumWays([29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38], 35), 0)
if __name__ == '__main__':
    unittest.main()
