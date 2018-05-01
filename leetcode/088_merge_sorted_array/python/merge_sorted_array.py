"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""
import bisect
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        sorted_length = m        
        for i in range(0,n):
            pos = bisect.bisect_left(nums1[:sorted_length], nums2[i])
            del nums1[-1]            
            nums1.insert(pos, nums2[i])
            sorted_length += 1
