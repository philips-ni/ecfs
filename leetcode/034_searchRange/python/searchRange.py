
class Solution(object):
    def searchRange(self, nums, target):
        length = len(nums)
        leftIdx = 0
        rightIdx = length - 1
        foundIdx = -1
        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) / 2
            # print "leftIdx : %d" % leftIdx
            # print "rightIdx : %d" % rightIdx
            if nums[midIdx] > target:
                rightIdx = midIdx - 1
            elif nums[midIdx] < target:
                leftIdx = midIdx + 1
            else:
                foundIdx = midIdx
                break
        if foundIdx == -1:
            return [-1,-1]

        leftMostIdx = foundIdx
        while leftMostIdx >= 0:
            if nums[leftMostIdx] == target:
                leftMostIdx -= 1
            else:
                leftMostIdx += 1
                break
        if leftMostIdx == -1:
            leftMostIdx = 0
            
        rightMostIdx = foundIdx
        while rightMostIdx < length:
            if nums[rightMostIdx] == target:
                rightMostIdx += 1
            else:
                rightMostIdx -= 1
                break
        if rightMostIdx == length:
            rightMostIdx = length - 1
            
        return [leftMostIdx, rightMostIdx]

        
                
