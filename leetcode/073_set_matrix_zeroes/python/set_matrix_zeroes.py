
class Solution(object):
    def setZeroes(self, l):
        if len(l) == 0:
            return l
        zeroPoss = self.findZeroes(l)
        for (i,j) in zeroPoss:
            self.setRowZero(l, i)
            self.setColZero(l, j)
    
    def findZeroes(self, l):
        zeroes = []
        for i in range(len(l)) :
            for j in range(len(l[0])):
                if l[i][j] == 0:
                    zeroes.append((i,j))
        return zeroes
    
    def setRowZero(self, l, i):
        l[i] = [0] * len(l[0])

    def setColZero(self, l, j):
        for i in range(len(l)):
            l[i][j] = 0        
            
