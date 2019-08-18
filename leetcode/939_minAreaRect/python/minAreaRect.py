from collections import defaultdict
class Solution1(object):
    def minAreaRect(self, points):
        dict_px = defaultdict(set)
        for p in points:
            dict_px[p[0]].add(p[1])
        minArea = float('inf')
        for k1 in dict_px:
            for k2 in dict_px:
                if k1 == k2:
                    continue
                minArea = min(minArea, self.getMinArea(dict_px, k1, k2))
        if minArea == float('inf'):
            return 0
        else:
            return minArea
    def getMinArea(self, dict_px, k1, k2):
        commons = dict_px[k1].intersection(dict_px[k2])
        if len(commons) < 2:
            return float('inf')
        commonsL = sorted(list(commons))
        minDelta = float('inf')
        for i in range(len(commonsL) - 1) :
            minDelta = min(minDelta, commonsL[i+1] - commonsL[i])
        if minDelta == float('inf'):
            return float('inf')
        else:
            return minDelta * abs(k2 - k1)


class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in xrange(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0
