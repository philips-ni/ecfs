"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
"""
class Solution:
# @return an integer
    def divide0(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = 0 - res
        return min(max(-2147483648, res), 2147483647)


    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res, power = 0, 32
        divisor_power = divisor << power
        while dividend >= divisor:
            while divisor_power > dividend:
                divisor_power >>= 1
                power -= 1
            res += 1 << power
            print "res: %d" % res
            dividend -= divisor_power
        if not positive:
            res = 0 - res
        return min(max(-2147483648, res), 2147483647)
    
