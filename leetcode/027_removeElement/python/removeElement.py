
class Solution(object):
    def removeElement(self, l, value):
        newTail = 0
        idx = 0
        while idx < len(l):
            if l[idx] == value:
                idx += 1
            else:
                l[newTail] = l[idx]
                newTail += 1
                idx += 1
        return newTail
        
