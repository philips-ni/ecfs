
class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n + 1)
        if n < 2:
            return 1
        dp[0] = 1
        dp[1] = 1        
        idx = 2
        while idx <= n:
            for j in range(0, idx):
                dp[idx] += dp[j] * dp[idx-1-j]
            idx += 1
        return dp[n]
