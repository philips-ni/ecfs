
class Solution(object):
    def isHappy(self, n, l=None):
        if l == None:
            l = list()
        if n in l:
            return False
        if n == 1:
            return True
        l.append(n)
        n1 = sum( (int(i) ** 2 for i in str(n) ))
        return self.isHappy(n1,l)
                       
        
