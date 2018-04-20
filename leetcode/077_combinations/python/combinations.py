class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l=list(range(1,n+1))
        allPaths=[]
        visited = []
        self.dfs(l,k,0,visited,allPaths)
        return allPaths
        
    def dfs(self,l,k,index,visited,allPaths):
        # print "index: %d , visited: %s, allPaths: %s" % (index, str(visited), str(allPaths))
        if len(visited)==k:
            allPaths.append(visited)
            # print "path founded"
            return 
        while len(l) - index >= k - len(visited):
            tmpVisited = visited + [l[index]]
            index += 1
            self.dfs(l,k,index,tmpVisited,allPaths)
