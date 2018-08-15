# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
# 
# Example:
# 
# Input: 
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 6 
# 
# Explanation: Given three people living at (0,0), (0,4), and (2,2):
#              The point (0,2) is an ideal meeting point, as the total travel distance 
#              of 2+2+2=6 is minimal. So return 6.
#
class Solution(object):
    def minTotalDistance(self, grid):
        rowL, colL = self.getRowAndColL(grid)
        if len(rowL) == 1 or len(colL) == 1:
            return 0
        if len(rowL) == 0:
            return -1
        mR = rowL[len(rowL) // 2]
        mC = colL[len(colL) // 2]
        d = 0
        for x in rowL:
            d += abs(x - mR)
        for y in colL:
            d += abs(y - mC)
        return d

    def getRowAndColL(self,grid):
        rowL = []
        colL = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rowL.append(i)
                    colL.append(j)
        return sorted(rowL), sorted(colL)
