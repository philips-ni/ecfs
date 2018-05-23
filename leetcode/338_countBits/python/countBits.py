"""
Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2].

Solution tips:

p(x) = p(x/2) + (x % 2)
p(x) = p(x & x-1) + 1
"""
class Solution(object):
    def countBits2(self, n):
        ret = [0]
        for i in range(1, n+1):
            ret.append(ret[i >> 1] + i % 2)
        return ret
    
    def countBits(self, n):
        ret = [0]
        for i in range(1, n+1):
            ret.append(ret[i & (i-1)] + 1)
        return ret
