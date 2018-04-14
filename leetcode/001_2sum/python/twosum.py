
"""
Summary: 2sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = self.convertToDict(nums)
        idx = 0
        found_it = False
        for n in nums:
            another_part = target - n
            if another_part in nums_dict:
                another_part_idxs = nums_dict[another_part]
                if n == another_part and len(another_part_idxs) == 1:
                    idx += 1
                    continue
                elif n == another_part:
                    another_part_idx = another_part_idxs[1]
                else:
                    another_part_idx = another_part_idxs[0]
                found_it = True
                break
            idx += 1
        if found_it :
            return [idx, another_part_idx]
        else:
            return []

    def convertToDict(self,nums):
        nums_dict = {}
        idx = 0
        for n in nums:
            if n in nums_dict:
                nums_dict[n].append(idx)
            else:
                nums_dict[n] = [idx]                
            idx += 1
        return nums_dict
