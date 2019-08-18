import unittest
import maxSlidingWindow

class TestMaxslidingwindow(unittest.TestCase):
    def test_maxSlidingWindow(self):
        s = maxSlidingWindow.Solution()
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3        
        self.assertEqual(s.maxSlidingWindow(nums, k), [3,3,5,5,6,7])
        
if __name__ == '__main__':
    unittest.main()
