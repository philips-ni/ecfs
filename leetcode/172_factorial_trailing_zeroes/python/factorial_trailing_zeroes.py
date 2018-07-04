"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
"""
class Solution(object):
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        else:
            return n/5 + self.trailingZeroes(n//5)

class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while n // 5**i > 0:
            count += n//5**i
            i += 1
        return count
