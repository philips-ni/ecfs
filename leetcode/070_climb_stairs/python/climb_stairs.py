
class Solution(object):
    def climbStairs0(self, n):
        dp = [1,1]
        if n < 2:
            return dp[n]
        i = 2
        while i <= n:
            dp.append(dp[i-1] + dp[i-2])
            i += 1
        return dp[n]
    
    def climbStairs1(self, n):
        # Fibnacci approch
        a,b = 1,1
        for i in range (n - 1):
            a,b=b,a+b
        return b
        
    def climbStairs(self, n):
        visited = []
        fullPaths = []
        self.dfs(n, 0, visited,fullPaths)
        print fullPaths
        return len(fullPaths)
    
    def dfs(self, n, i, visited, fullPaths):
        # print "n: %d" % n
        # print "i: %d" % i
        # print visited
        if i > n:
            # print "cannot go beyond"
            return
        elif i == n:
            visited.append(i)
            # print "found a path"
            fullPaths.append(visited)
            # print visited
            return
        else:
            visited.append(i)
            curPath = visited[:]
            self.dfs(n, i + 1 , visited, fullPaths)
            visited = curPath
            self.dfs(n, i + 2 , visited, fullPaths)
            
