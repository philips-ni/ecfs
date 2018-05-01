
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

"""

class Solution(object):
    def countAndSay(self, n):
        if n == 1: return "1"
        s = self.countAndSay(n-1)
        i, ch, tmp = 0, s[0], ''
        for j in range(1, len(s)):
            if s[j] != ch:
                tmp += str(j-i) + ch
                i, ch = j, s[j]
        tmp += str(len(s)-i) + ch
        return tmp
    
    def countAndSay2(self, n):
        dp = ["0","1"]
        idx = 2
        while idx <= n:
            # print("idx: %d" % idx)
            dp.append(self.getCS(dp[idx - 1]))
            idx += 1
        return dp[n]

    def getCS(self, nStr):
        nlist = []
        n = int(nStr)
        while n > 0:
            div = n / 10
            remainder = n % 10
            nlist.insert(0, remainder)
            n = div
        length = len(nlist)
        idx = 1
        prevN = nlist[0]
        counter = 1
        retS = ""
        while idx < length:
            if nlist[idx] == prevN:
                counter += 1
            else:
                retS += "%d%d" % (counter, prevN)
                prevN = nlist[idx]
                counter = 1
            idx += 1
        retS += "%d%d" % (counter, prevN)
        return retS
    
