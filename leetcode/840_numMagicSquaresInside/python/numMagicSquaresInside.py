
class Solution(object):
    def numMagicSquaresInside(self, d):
        rows = len(d)
        if rows < 3:
            return 0
        cols = len(d[0])
        if cols < 3:
            return 0
        counter = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if self.isMagic(d,r,c):
                   counter += 1
        return counter

    def isMagic(self, d, r, c):
        if d[r][c] + d[r+2][c+2] == d[r][c+2] + d[r+2][c]:
            s = set()
            for i in range(3):
                for j in range(3):
                    if d[r+i][c+j] < 1 or d[r+i][c+j] > 9:
                        return False                    
                    if d[r+i][c+j] not in s:
                        s.add(d[r+i][c+j])
                    else:
                        return False
            if sum([ d[r][c],d[r+1][c],d[r+2][c] ]) == sum([ d[r][c+1],d[r+1][c+1],d[r+2][c+1] ]) == sum([ d[r][c+2],d[r+1][c+2],d[r+2][c+2] ]) and \
                sum([ d[r][c],d[r][c+1],d[r][c+2] ]) == sum([ d[r+1][c],d[r+1][c+1],d[r+1][c+2] ]) == sum([ d[r+2][c],d[r+2][c+1],d[r+2][c+2] ]):
                # self.printSubGrid(d,r,c)
                return True
        else:
            return False
        
    def printSubGrid(self,d,r,c):
        for i in range(3):
            for j in range(3):
                print("%d " % d[r+i][c+j], end = '')
            print("\n")
