"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        if len(nums) <= 3:
            return sum(nums)
        answer = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) -2):
            j = i + 1
            k = len(nums) -1
            while j < k:
                candidateAnswer = nums[i] + nums[j] + nums[k]
                if abs(target - candidateAnswer) < abs(target - answer) :
                    answer = candidateAnswer
                if target - candidateAnswer == 0:
                    return candidateAnswer
                elif target - candidateAnswer > 0:
                    j += 1
                else:
                    k -= 1
        return answer
                
        
