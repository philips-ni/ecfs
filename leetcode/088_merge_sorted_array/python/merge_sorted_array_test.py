
import unittest
import merge_sorted_array

class TestMerge_Sorted_Array(unittest.TestCase):
    def test_merge(self):
        s = merge_sorted_array.Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        s.merge(nums1,m,nums2,n)
        print nums1

        nums1 = [0,0,0]
        m = 0
        nums2 = [2,5,6]
        n = 3
        s.merge(nums1,m,nums2,n)
        print nums1
        
if __name__ == '__main__':
    unittest.main()
