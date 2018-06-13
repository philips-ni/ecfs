"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from collections import defaultdict
class Solution(object):
    def wordBreak2(self, s, wordDict):
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] not in wordDict:
                continue
            else:
                if self.wordBreak(s[i:], wordDict):
                    return True
        return False

    def wordBreak(self, s, words):
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        return dp[-1]    
