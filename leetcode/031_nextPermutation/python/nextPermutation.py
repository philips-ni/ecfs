
class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        if length < 2:
            return
        
        currIdx = length - 2
        nextIdx = currIdx + 1
        while currIdx >= 0 :
            if nums[currIdx] >= nums[nextIdx]:
                currIdx -= 1
                nextIdx -= 1
            else:
                break
        # Find the first num which is less than nums[currIdx] and get its idx
        # print "currIdx: %d" % currIdx
        if currIdx == -1:
            nums.sort()
            return
        
        swappingIdx = currIdx + 1
        while swappingIdx < length:
            if nums[swappingIdx] > nums[currIdx]:
                    swappingIdx += 1
            else:
                swappingIdx -= 1
                break
        if swappingIdx == length:
            swappingIdx -= 1
        # print "swappingIdx: %d" % swappingIdx
        self.swap(nums, currIdx, swappingIdx)

        # Reverse part of list, nums[currIdx + 1: length]
        middleIdx = currIdx + (length - currIdx -1)/2
        leftIdx = currIdx + 1
        rightIdx = length - 1
        while leftIdx < rightIdx:
            self.swap(nums, leftIdx, rightIdx)
            leftIdx += 1
            rightIdx -= 1
            
    def swap(self,nums, idx1,idx2):
        if idx1 < 0 or idx1 > len(nums) - 1:
            print "idx1: %d is invalid"
            return
        if idx2 < 0 or idx2 > len(nums) -1:
            print "idx2: %d is invalid"            
            return
        if idx1 != idx2 :
            tmp = nums[idx1]
            nums[idx1] = nums[idx2]
            nums[idx2] = tmp
        
