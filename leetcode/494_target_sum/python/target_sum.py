class Solution(object):
    def findTargetSumWays3(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)
    
    def findTargetSumWays2(self, nums, S):
        if len(nums) == 1:
            if abs(S) == nums[0]:
                if nums[0] == 0:
                    return 2
                else:
                    return 1
            else:
                return 0
        else:
            return self.findTargetSumWays(nums[:-1], S + nums[-1]) + \
                self.findTargetSumWays(nums[:-1], S - nums[-1])
                
