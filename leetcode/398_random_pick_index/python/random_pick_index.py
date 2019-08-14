import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
    def pick(self, target):
        start_idx = random.choice(range(0,len(self.nums)))
        # print("start_idx: {}".format(start_idx))
        i = j = start_idx
        ret = -1
        while i >= 0 and j < len(self.nums):
            # print("i: {},j: {}".format(i,j))
            if self.nums[i] == target:
                ret = i
                break
            if self.nums[j] == target:
                ret = j
                break
            if i > 0 :
                i -= 1
            if j < len(self.nums) -1:
                j += 1
        # print("ret: {}".format(ret))
        return ret
            

