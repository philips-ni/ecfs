"""
Calculate the sum of two positive integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
class Solution(object):
    def getSum(self, a, b):
        while a != 0 and b != 0:
            tmp = a ^ b
            b = (a & b ) << 1
            a = tmp
        if a == 0:
            return b
        else:
            return a
