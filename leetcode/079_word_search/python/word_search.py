import pprint
class Solution(object):
    def is_valid(self, i, j, board):
        m, n  = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        return True

    def dfs(self, i, j, k, visited, board, word):
        print "i: %d" % i
        print "j: %d" % j
        print "k: %d" % k
        pp = pprint.PrettyPrinter(depth=6)
        print "visited: "
        pp.pprint(visited)
        
        if (i, j) in visited:
            return False

        if board[i][j] != word[k]:
            return False

        if k + 1 == len(word):
            return True

        visited.add((i, j))
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if self.is_valid(ni, nj, board) and self.dfs(ni, nj, k+1, visited, board, word):
                return True
        visited.remove((i, j))

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        m, n  = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                visited = set()
                if self.dfs(i, j, 0, visited, board, word):
                    return True
        return False
