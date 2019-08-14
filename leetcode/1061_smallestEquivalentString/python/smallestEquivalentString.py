import collections
class Solution1(object):
    def smallestEquivalentString(self, A, B, S):
        # Setup the graph with the equlity relationship
        graph = collections.defaultdict(set)
        for i in range(len(A)):
            graph[A[i]].add(B[i])
            graph[B[i]].add(A[i])
        memo = {}
        
        def dfs(c, vis):
            if c in memo:
                return memo[c]
            res = c
            for n in graph[c]:
                if n not in vis:
                    vis.add(n)
                    res = min(res, dfs(n, vis))
            return res

        res = ''
        for c in S:
            vis = set()
            new_c = dfs(c, vis)
            for c in vis:
                memo[c] = new_c
            res += new_c
        return res
            
                       

class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        letters = "abcdefghijklmnopqrstuvwxyz"
        data = [ i for i in range(26)] 
        rank = [ i for i in range(26)]
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        
        def union(x, y):
            x_r = find(x)
            y_r = find(y)
            if rank[x_r] <= rank[y_r]:  # union to the smaller rank one for lexicographically smallest output
                data[y_r] = x_r
            elif rank[y_r] < rank[x_r]:
                data[x_r] = y_r
        
        for i in range(len(A)):
            union(ord(A[i])-97, ord(B[i])-97)
        res=""
        for i in S:
            res += letters[(find(ord(i)-97))]
            
        return res    
