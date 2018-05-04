class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # print "m= %d,n=%d" % (m,n)
        from collections import defaultdict
        store = defaultdict(dict)
        return self.dfs(m,n,0,0,obstacleGrid,store)

    def dfs(self,m,n,i,j,obstacleGrid, store):
        # print "i: %d, j: %d" % (i,j)
        if obstacleGrid[i][j] == 1:
            return 0        
        if i == m - 1 and j == n -1:
            return 1
        if i >= m - 1:
            return self.dfs(m,n,i,j+1,obstacleGrid,store)
        if j >= n - 1:
            return self.dfs(m,n,i+1,j,obstacleGrid,store)
        if j not in store[i]:
            store[i][j] = self.dfs(m, n, i+1, j, obstacleGrid, store) + self.dfs(m,n,i,j+1,obstacleGrid,store)
        return store[i][j]
