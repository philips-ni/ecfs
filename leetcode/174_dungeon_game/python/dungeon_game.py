import sys
class Solution(object):
    def calculateMinimumHP(self, l):
        m = len(l)
        n = len(l[0])
        r = [ [sys.maxint] * (n + 1) for _ in range(0, m + 1) ]
        r[m][n-1] = 1
        r[m-1][n] = 1
        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):                
                r[i][j] = min(r[i+1][j], r[i][j+1]) - l[i][j]
                if r[i][j] <= 0:
                    r[i][j] = 1
        return r[0][0]
                
