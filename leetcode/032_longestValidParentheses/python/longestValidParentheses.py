"""
let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
dp[i + 1] = dp[p] + i - p + 1 where p is the position of ‘(’ which can matches current ‘)’ in the stack.
"""
class Solution(object):
    def longestValidParentheses(self, s):
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)    
