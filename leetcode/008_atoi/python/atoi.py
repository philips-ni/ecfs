"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""
MAX = 2147483647
MIN = -2147483648
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        startIdx = self.findStartIdx(str)
        print "startIdx: %d" % startIdx
        if startIdx == -1:
            return 0
        isNeg = False
        n = 0
        if str[startIdx] == "-":
            isNeg = True
        elif str[startIdx] == "+":
            n = 0
        else:
            n = int(str[startIdx])
        endIdx = self.findEndIdx(str, startIdx)
        print "endIdx: %d" % endIdx        
        if startIdx == endIdx:
            return n
        
        idx = startIdx + 1
        while idx <= endIdx:
            n = n * 10 + int(str[idx])
            idx += 1
        if isNeg:
            n = -1 * n
        if n > MAX:
            n = MAX
        elif n < MIN:
            n = MIN
        return n

    def findStartIdx(self,str):
        candidates = ['+','-','0','1','2','3','4','5','6','7',
                      '8','9'
                      ]
        for idx in range(0, len(str)):
            if str[idx] == ' ':
                idx += 1
                continue
            elif str[idx] not in candidates:
                return -1
            else:
                return idx
        return -1
    
    def findEndIdx(self, str, startIdx):
        candidates = ['0','1','2','3','4','5','6','7',
                      '8','9'
                      ]
        
        endIdx = startIdx
        for idx in range(startIdx + 1, len(str)):
            # print "str[%d]: %s" %(idx, str[idx])
            if str[idx] not in candidates:
                break
            else:
                endIdx = idx
                idx += 1
        return endIdx

