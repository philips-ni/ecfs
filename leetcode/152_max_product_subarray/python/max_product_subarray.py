class Solution(object):
    def maxProduct(self,nums):
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum
