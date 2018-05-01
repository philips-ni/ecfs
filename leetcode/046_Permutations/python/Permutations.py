
class Solution(object):
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

                
            
            
                        
                             
                             
