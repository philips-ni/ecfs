
class Solution(object):
    def trap(self, nums):
        length = len(nums)
        if length < 3:
            return 0
        
        leftMaxArray = [0] * length
        rightMaxArray = [0] * length        
        sum = 0
        
        iterIdx = length - 2
        rightMaxArray[length -1] = nums[length - 1]
        while iterIdx >= 0:
            rightMaxArray[iterIdx] = max(rightMaxArray[iterIdx + 1], nums[iterIdx])
            iterIdx -= 1

        iterIdx = 1
        leftMaxArray[0] = nums[0]
        while iterIdx < length:
            leftMaxArray[iterIdx] = max(leftMaxArray[iterIdx - 1], nums[iterIdx])
            sum += (min(leftMaxArray[iterIdx], rightMaxArray[iterIdx]) - nums[iterIdx])
            iterIdx += 1
        return sum
         
