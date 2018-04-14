import unittest
import medianTwoArray

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_findMedianSortedArrays1(self):
        s = medianTwoArray.Solution()
        nums1 = [1,3]
        nums2 = [2]
        expected_ret = 2.0
        self.assertEqual(expected_ret, s.findMedianSortedArrays(nums1, nums2)), 

    def test_findMedianSortedArrays2(self):
        s = medianTwoArray.Solution()
        nums1 = [1,2]
        nums2 = [3,4]
        expected_ret = 2.5
        self.assertEqual(expected_ret, s.findMedianSortedArrays(nums1, nums2)), 

    def test_findMedianSortedArrays3(self):
        s = medianTwoArray.Solution()
        nums1 = [1,2,2] 
        nums2 = [3,4]
        expected_ret = 2.0
        self.assertEqual(expected_ret, s.findMedianSortedArrays(nums1, nums2)), 


    def test_findMedianSortedArrays4(self):
        s = medianTwoArray.Solution()
        nums1 = [5] 
        nums2 = [6]
        expected_ret = 5.5
        self.assertEqual(expected_ret, s.findMedianSortedArrays(nums1, nums2)), 

    def test_findMedianSortedArrays5(self):
        s = medianTwoArray.Solution()
        nums1 = [] 
        nums2 = [6]
        expected_ret = 6.0
        self.assertEqual(expected_ret, s.findMedianSortedArrays(nums1, nums2)), 
        
        
if __name__ == '__main__':
    unittest.main()
