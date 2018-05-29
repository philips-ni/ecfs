"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2  times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from collections import defaultdict
class Solution(object):
    def majorityElement(self, l):
        count_dict = defaultdict(int)
        for i in l:
            count_dict[i] += 1
        for k in count_dict:
            if count_dict[k] > len(l) / 2:
                return k
        return None
