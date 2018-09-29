
import unittest
import CreateMaximumNumber

class TestCreatemaximumnumber(unittest.TestCase):
    def test_maxNumber(self):
        s = CreateMaximumNumber.Solution()
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        self.assertEqual(s.maxNumber(nums1,nums2,5), [9, 8, 6, 5, 3])
        self.assertEqual(s.maxNumber(nums1,nums2,4), [9, 8, 6, 5])
        self.assertEqual(s.maxNumber(nums1,nums2,3), [9, 8, 6])
        self.assertEqual(s.maxNumber(nums1,nums2,2), [9, 8])

        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        self.assertEqual(s.maxNumber(nums1,nums2,5), [6,7,6,0,4])

        nums1 = [3, 9]
        nums2 = [8, 9]
        self.assertEqual(s.maxNumber(nums1,nums2,3), [9,8,9])
        
if __name__ == '__main__':
    unittest.main()
