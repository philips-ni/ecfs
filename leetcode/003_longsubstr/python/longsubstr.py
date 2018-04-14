"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        startIdx = 0
        helperDict = {}
        idx = 0
        while idx < len(s):
            if s[idx] not in helperDict:
                if idx == len(s) -1 :
                    endIdx = idx
                    maxLen = max(maxLen, endIdx - startIdx + 1)
                else:
                    helperDict[s[idx]] = idx
            else:
                endIdx = idx - 1
                maxLen = max(maxLen, endIdx - startIdx + 1)
                # self.printSubStr(s, startIdx, idx - 1)
                startIdx =  helperDict[s[idx]] + 1
                helperDict = self.resetHelper(s, startIdx, idx)
            idx += 1
        return maxLen

    def resetHelper(self, s, startIdx, endIdx):
        helperDict = {}
        for idx in range(startIdx, endIdx + 1):
            helperDict[s[idx]] = idx
        return helperDict

    def printSubStr(self,s, startIdx, endIdx):
        print s[startIdx:endIdx+1]
        
