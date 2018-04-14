import unittest
import twosum

class TestTwoSum(unittest.TestCase):

    def test_twoSum(self):
        nums = [2,7,11,15,100]
        target1 = 9
        target2 = 10
        target3 = 17
        target4 = 115
        s = twosum.Solution()
        self.assertEqual(s.twoSum(nums,target1), [0,1])
        self.assertEqual(s.twoSum(nums,target2), [])
        self.assertEqual(s.twoSum(nums,target3), [0,3])
        self.assertEqual(s.twoSum(nums,target4), [3,4])


    def test_twoSum2(self):
        nums = [3,2,4]
        target = 6
        s = twosum.Solution()
        self.assertEqual(s.twoSum(nums,target), [1,2])

    def test_twoSum3(self):
        nums = [3,3]
        target = 6
        s = twosum.Solution()
        self.assertEqual(s.twoSum(nums,target), [0,1])
        
if __name__ == '__main__':
    unittest.main()
