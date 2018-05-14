"""
the idea is :
[1,...,first_product(n-2), first_product(n-1)] * [last_product(n-1),....last_product(1),last_product(0),1]
"""
class Solution(object):
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        # in this time, output will contain [1,...,first_product(n-2), first_product(n-1)]
        # print output
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output    
