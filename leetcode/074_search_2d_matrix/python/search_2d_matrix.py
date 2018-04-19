import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        rowLength = len(matrix)
        if rowLength == 0:
            return False
        colLength = len(matrix[0])
        if colLength == 0:
            return False
        firstCol = self.getFirstCol(matrix)
        candidateRowIdx, foundIt = self.getRowIdx(firstCol, target)
        if candidateRowIdx == -1:
            return False
        if foundIt :
            return True
        i = bisect.bisect_left(matrix[candidateRowIdx], target)
        if i != colLength and matrix[candidateRowIdx][i] == target:
            return True
        else:
            return False
    def getFirstCol(self,matrix):
        firstCol = []
        for i in range(len(matrix)):
            firstCol.append(matrix[i][0])
        return firstCol

    def getRowIdx(self, l, target):
        idx = bisect.bisect_left(l, target)
        if idx < len(l) and l[idx] == target:
            return (idx, True)
        else:
            return (idx - 1, False)
            
