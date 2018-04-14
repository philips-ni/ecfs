
import unittest
import threeSumClosest

class TestThreesumclosest(unittest.TestCase):
    def test_threeSumClosest(self):
        s = threeSumClosest.Solution()
        nums = [-1,2,1,-4]
        target = 1
        self.assertEqual(2, s.threeSumClosest(nums, target))

    def test_threeSumClosest2(self):
        s = threeSumClosest.Solution()
        nums = [0,0,0]
        target = 1
        self.assertEqual(0, s.threeSumClosest(nums, target))

    def test_threeSumClosest3(self):
        s = threeSumClosest.Solution()
        nums = [0,0,0,1,2,3]
        target = 1
        self.assertEqual(1, s.threeSumClosest(nums, target))
        
if __name__ == '__main__':
    unittest.main()
