from collections import Counter
class Solution(object):
    def leastBricks(self, wall):
        if len(wall) == 0:
            return 0
        if len(wall) == 1 :
            if len(wall[0]) > 1:
                return 0
            else:
                return 1
        inEdgesWall = []
        for row in wall:
            inEdges = self.getInEdges(row)
            inEdgesWall.append(inEdges)
        # print(inEdgesWall)
        mostCommonEdge = self.getMostCommonEdge(inEdgesWall)
        return len(wall) - mostCommonEdge
    
    def getInEdges(self, row):
        edges = []
        pos = 0
        for i in row[:-1]:
            pos += i
            edges.append(pos)
        return edges

    def getMostCommonEdge(self, inEdgesWall):
        cnt = Counter()
        for edges in inEdgesWall:
            for e in edges:
                cnt[e] += 1
        if len(cnt.keys()) == 0:
            return 0
        mc = cnt.most_common(1)[0]
        # print("mc: {}".format(mc))
        return mc[1]
        
