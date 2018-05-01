
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        leftIdx = 0
        rightIdx = len(nums) - 1
        retIdx = -1
        while leftIdx <= rightIdx:
#            print "leftIdx : %d" % leftIdx
#            print "rightIdx : %d" % rightIdx
            midIdx = (leftIdx + rightIdx ) / 2
#            print "midIdx : %d" % midIdx                        
            if nums[midIdx] < target:
                if midIdx < len(nums) - 1 and nums[midIdx + 1] > target:                
                    retIdx = midIdx + 1
                    break
                else:
                    leftIdx = midIdx + 1
            elif nums[midIdx] > target:
                if midIdx > 1 and nums[midIdx - 1] < target:                
                    retIdx = midIdx
                    break
                else:
                    rightIdx = midIdx - 1
            else:
                retIdx = midIdx
                break
        if retIdx == -1 :
            if rightIdx == len(nums) - 1:
                return len(nums)
            else:
                return 0
        else:
            return retIdx
        
                
        
