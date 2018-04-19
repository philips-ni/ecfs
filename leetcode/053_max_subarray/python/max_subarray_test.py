
import unittest
import max_subarray

class TestMax_Subarray(unittest.TestCase):
    def test_maxSubArray(self):
        s = max_subarray.Solution()
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray([1]), 1)
        self.assertEqual(s.maxSubArray([-1,2]), 2)
        self.assertEqual(s.maxSubArray([]), 0)
        self.assertEqual(s.maxSubArray([-1]), -1)                        

if __name__ == '__main__':
    unittest.main()
