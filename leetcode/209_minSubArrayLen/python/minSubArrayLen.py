import sys
from collections import defaultdict
MAX_INT=sys.maxint
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum == s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution0(object):
    def minSubArrayLen(self, s, nums):
        sums_dict = defaultdict(int)
        sums = []
        sumV = 0
        for i, n in enumerate(nums):
            sumV += n
            sums_dict[sumV] = i
            sums.append(sumV)
        min_len = MAX_INT
        for i, n in enumerate(sums):
            tmp = n + s
            if tmp in sums_dict:
                min_len = min(min_len, sums_dict[tmp] - i)
        if min_len == MAX_INT:
            min_len = 0
        return min_len
        
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        ans = MAX_INT
        sumV = 0
        left = 0
        for i, n in enumerate(nums):
            sumV += n
            while sumV >= s:
                # print("sumV: {}, i: {}, left :{}".format(sumV, i,left))
                ans = min(ans, i - left + 1)                
                sumV -= nums[left]
                left += 1
        if ans == MAX_INT:
            ans = 0
        return ans 
            

            
        
        
