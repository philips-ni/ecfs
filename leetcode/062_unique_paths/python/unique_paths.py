import pprint
class Solution2(object):
    def uniquePaths(self, m, n):
        pathCounter = [0]
        self.dfs(m,n,0,0,pathCounter)
        return pathCounter[0]

    def dfs(self, m, n, rIdx, cIdx, pathCounter):
        if rIdx == m - 1 and cIdx == n - 1:
            pathCounter[0] += 1
            return
        if rIdx < m -1:
            self.dfs(m, n,  rIdx + 1, cIdx, pathCounter)
        if cIdx < n -1:
            self.dfs(m, n,  rIdx, cIdx + 1, pathCounter)
            
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        store = defaultdict(dict)
        return self.uniqueP(m, n, 1, 1, store)


    def uniqueP(self, m, n, x, y, store):
        """
        x, y represent robot position
        """
        # print store        
        if x == m and y == n:
            return 1

        if x >= m:
            return self.uniqueP(m, n, x, y+1, store)

        if y >= n:
            return self.uniqueP(m, n, x+1, y, store)

        if y not in store[x]:
            store[x][y] = self.uniqueP(m, n, x+1, y, store) + self.uniqueP(m, n, x, y+1, store)
        # pp = pprint.PrettyPrinter(depth=6)
        #pp.pprint(store)
        return store[x][y]
