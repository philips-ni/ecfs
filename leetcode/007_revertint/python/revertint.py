"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
MAX = 2147483647
MIN = -2147483648
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        absX = x
        if x < 0:
            isNeg = True
            absX = -1 * x
        xList = []
        tmp = absX
        while tmp > 0:
             xList.append( tmp % 10)
             tmp = tmp / 10
        ret = 0
        for idx in range(0, len(xList)):
            ret += xList[idx] * pow(10, len(xList) - 1 - idx)
        if isNeg :
            ret = -1 * ret
        if ret > MAX or ret < MIN:
            ret = 0
        return ret
                                    
