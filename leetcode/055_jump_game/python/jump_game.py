"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
class Solution(object):
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        counter = 0
        for i in nums[::-1]:
            if i >= counter:
                tag = True
                counter = 1
            else:
                tag = False 
                counter += 1
        return tag
    
    def canJump(self, nums):
        zeroPositions = self.findZeroPoss(nums)
        if len(zeroPositions) == 0:
            return True

        if zeroPositions[-1] == len (nums) -1:
            zeroPositions.pop()

        for pos in zeroPositions:
            if self.isBlockingZero(nums, pos):
                return False
        return True
    
    def findZeroPoss(self, nums):
        poss = []
        for i,n in enumerate(nums):
            if n == 0:
                poss.append(i)
        return poss
                
    def isBlockingZero(self, nums, pos):
        if pos == 0:
            return True
        idx = 0
        while idx < pos:
            if idx + nums[idx] > pos:
                break
            idx += 1
        if idx == pos:
            return True
        else:
            return False
