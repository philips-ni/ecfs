
class Solution1(object):
    def permute(self, l):
        return self._permute(l,len(l))
                             
    def _permute(self, l, n):
        if n ==  0:
            return [[]]
        if n == 1:
            return [l[:n]]
        retL = []
        for subL in self._permute(l, n - 1):
            retL.append(subL + [l[n-1]])
            retL.append([l[n-1]] + subL)
            for i in xrange(1, n - 1):
                tmpL = subL[:i] + [l[n-1]] + subL[i:]
                retL.append(tmpL)
        return retL


class Solution(object):
    def permute(self, l):
        if len(l) == 0:
            return [[]]
        permuations = []
        curr = []
        isVisited = [False] * len(l)
        self.backTracking(permuations, curr, isVisited, l)
        return permuations
    
    def backTracking(self, permuations,  curr, isVisited, l):
        if len(curr) == len(l):
            permuations.append(curr[:])
            return

        for i in range(len(l)):
            if not isVisited[i]:
                isVisited[i] = True
                curr.append(l[i])
                self.backTracking(permuations, curr, isVisited, l)
                isVisited[i] = False
                curr.pop()
