def swap(nums, i, j):
    tmp = nums[j]
    nums[j] = nums[i]    
    nums[i] = tmp

class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return
        idx = 0
        while idx < len(nums):
            if nums[idx] == 0:
                break
            idx += 1
        if idx == len(nums):
            return
        last_nz_idx = idx - 1
        idx += 1
        while idx < len(nums):
            if nums[idx] != 0:
                swap(nums,last_nz_idx + 1, idx)
                last_nz_idx += 1
            idx+=1
