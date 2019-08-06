
class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while end >= start:
            middle = (start + end) // 2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return middle
        return -1
            
