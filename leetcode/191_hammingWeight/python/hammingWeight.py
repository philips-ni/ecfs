"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
"""
class Solution(object):
    def hammingWeight2(self,n):
        if n == 0:
            return 0
        if n % 2 == 1:
            return self.hammingWeight( n >> 1) + 1
        else:
            return self.hammingWeight( n >> 1)
    def hammingWeight(self,n):
        count = 0
        while n != 0:
            n = n & (n-1)
            count += 1
        return count
