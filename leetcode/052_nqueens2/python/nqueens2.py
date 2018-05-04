class Solution(object):
    def totalNQueens(self, n):
        if n == 0:
            return 0
        self.counter = 0
        self.dfs(n, [])
        return self.counter
    
    def dfs(self,n,placed_queens):
        length = len(placed_queens)
        if length == n:
            self.counter += 1
            return
        for i in range(0,n):
            if self.isAllowed(n, i,placed_queens):
                self.dfs(n,placed_queens + [i])

    def isAllowed(self, n, i, placed_queens):
        length = len(placed_queens)
        # To check if this pos [i,length] is a allowed
        for col, row in enumerate(placed_queens):
            if i == row:
                return False
            if abs(i-row) == abs(length - col):
                return False
        return True
