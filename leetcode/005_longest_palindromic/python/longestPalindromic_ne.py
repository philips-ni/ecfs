"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 

Example:

Input: "cbbd"

Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.isPal(s):
            return s
        
        startIdx = 0
        maxDict = {"maxlen": 0,
                   "sstr": ""}
        lenOfS = len(s)
        while startIdx < lenOfS and maxDict["maxlen"] < (lenOfS - maxDict["maxlen"] + 1):
            sstrDict = self.lenOfPal(s,startIdx)
            if sstrDict["maxlen"] > maxDict["maxlen"]:
                maxDict = {
                    "maxlen": sstrDict["maxlen"],
                    "sstr": sstrDict["sstr"]
                }
            print "startIdx: %d" % (startIdx)
            startIdx += 1
        return maxDict["sstr"]

    def lenOfPal(self,s, startIdx):
        """
        :desc: to find the max length PAL num start from the pos startIdx
        :type s: str
        :type startIdx: int
        :rtype : int, the length
        """
        
        lIdx = startIdx
        possibleRendIdx = self.getPosFromBack(s, lIdx, len(s) -1)
        rIdx = possibleRendIdx
        while lIdx < rIdx :
            if s[lIdx] == s[rIdx]:
                print "in %d,%d, matched" % (lIdx, rIdx)
                lIdx += 1
                rIdx -= 1
            else:
                # print "in %d,%d, not match, reset idxs" % (lIdx, rIdx)
                lIdx = startIdx
                possibleRendIdx = self.getPosFromBack(s, lIdx, possibleRendIdx -1)
                rIdx = possibleRendIdx
        maxlen = possibleRendIdx - startIdx + 1
        sstr = s[startIdx:possibleRendIdx+1]
        ret = {"maxlen" : maxlen,
               "sstr": sstr}
        return ret
            
    def getPosFromBack(self, s, lIdx, rIdx):
        """
        :desc: to find the pos in the range s[lIdx: rIdx + 1], in which pos, the element value is equal to s[lIdx]
        :type s: str
        :type lIdx: the left side idx of substr of s
        :type rIdx: the right side idx of substr of s
        :rtype: int
        """
        posIdx = rIdx
        c = s[lIdx]
        while posIdx > lIdx:
            if s[posIdx] == c:
                break
            else:
                posIdx -= 1
        # print "possible pos: %d, char: %s" % (posIdx, s[posIdx])
        return posIdx
            
    def isPal(self, s):
        lIdx = 0
        rIdx = len(s) -1
        ret = True
        while lIdx < rIdx:
            if s[lIdx] == s[rIdx]:
                lIdx += 1
                rIdx -= 1
            else:
                ret = False
                break
        return ret
