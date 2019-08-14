from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        a_xor_b = reduce(lambda x, y: x ^ y, nums)
        xor_sum = dict()
        for a in nums:
            b = a_xor_b ^ a
            if b in xor_sum and xor_sum[b] == a:
                return [b,a]
            xor_sum[a] = b
        
