import collections
class Solution(object):
    def sortColors(self,nums):
        counter = collections.Counter(nums)
        for i in range(len(nums)):
            if i >= counter[0] + counter[1]: nums[i] = 2
            elif i >= counter[0]: nums[i] = 1
            else: nums[i] = 0
