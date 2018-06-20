class Solution(object):
    def solveNQueens(self, n):
        if n == 0:
            return []
        solutions = []
        self.dfs(n, [], solutions)
        # print solutions
        return self.convert(solutions)
    
    def dfs(self,n,placed_queens,solutions):
        # print placed_queens
        length = len(placed_queens)
        if length == n:
            # print "found it"
            solutions.append(placed_queens)
            return  # backtrack
        for i in range(0,n):
            if self.isAllowed(n, i,placed_queens):
                self.dfs(n,placed_queens + [i],solutions)
            else:
                pass # backtrack

    def isAllowed(self, n, i, placed_queens):
        length = len(placed_queens)
        for col, row in enumerate(placed_queens):
            if i == row:
                return False
            if abs(i-row) == abs(length - col):
                return False
        return True

    def convert(self,solutions):
        if len(solutions) == 0:
            return []
        out = []
        item_tpl = ["."] * len(solutions[0])
        for s in solutions:
            s_item = []
            for i in s:
                item = item_tpl[:]
                item[i] = "Q"
                s_item.append(''.join(item))
            out.append(s_item)
        return out
