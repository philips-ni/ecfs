class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [ [0 for _ in range(cols)] for _ in range(rows)]
        max_side_len = float("-inf")
        for i in range(rows):
            for j in range(cols):
                print("dp: {}".format(dp))
                print("i: {}".format(i))
                print("j: {}".format(j))                    
                if i == 0 or j==0 or int(matrix[i][j]) == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side_len = max(max_side_len, dp[i][j])
        return max_side_len * max_side_len

