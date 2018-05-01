"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, l):
        ret = l
        if len(l) == 0:
            return [1]
        if l[-1] == 9:
            return self.plusOne(l[:-1]) + [0]
        else:
            return l[:-1] + [l[-1] + 1]
        
