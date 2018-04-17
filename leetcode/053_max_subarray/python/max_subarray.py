"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        length = len(nums)
        idx = 0
        maxSum = 0
        currSum = 0
        maxNum = nums[0] if len(nums) > 0 else 0
        while idx < len(nums):
            if currSum + nums[idx] > 0:
                currSum += nums[idx]
            else:
                currSum = 0
            maxNum = max(maxNum, nums[idx])
            maxSum = max(maxSum, currSum)
            idx += 1
        
        if maxSum == 0:
            # if all number less equal to 0,  just return max num
            return maxNum
        else:
            return maxSum
        
