"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1->3->1->1->1 minimizes the sum.
"""
import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        d = [[0]*n]*m
        dd = float("inf") # positive infinite
        for i in range(n):
            d[0][i] = grid[0][i] + (d[0][i-1] if i-1 >=0 else 0)
        for i in range(1,m):
            for j in range(n):
                d[i][j] = min((d[i-1][j] if i-1 >=0 else dd), (d[i][j-1] if j-1>=0 else dd) ) + grid[i][j]
        return d[m-1][n-1]
    
    def minPathSum2(self, grid):
        visited = []
        store = {
            "minPathSum": sys.maxint,
            "minPath" : []
        }
        m = len(grid)
        n = len(grid[0])
        self.dfs(grid, m, n, 0, 0, visited, store)
        return store["minPathSum"]
    
    def pathSum(self, grid, path):
        sum = 0
        for (i,j) in path:
            sum += grid[i][j]
        return sum
        
    def dfs(self, grid, m, n, i, j, visited, store):
        newVisited = visited[:]
        newVisited.append((i,j))
        currentPathSum = self.pathSum(grid, newVisited)
        if  currentPathSum >= store["minPathSum"]:
            return  #backtrack
        if i == m - 1 and j == n - 1:
            if currentPathSum < store["minPathSum"]:
                store["minPath"] = newVisited
                store["minPathSum"] = currentPathSum
            return
        elif i == m - 1:
            self.dfs(grid, m, n, i, j + 1, newVisited, store)
        elif j == n - 1:
            self.dfs(grid, m, n, i + 1, j, newVisited, store)
        else:
            self.dfs(grid, m, n, i, j + 1, newVisited, store)            
            self.dfs(grid, m, n, i + 1, j, newVisited, store)
            
            
