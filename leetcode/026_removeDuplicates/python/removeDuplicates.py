
class Solution(object):
    def removeDuplicates(self, l):
        length = len(l)
        if length < 2:
            return length
        newTail = 0

        # find the diff one comparing with existing tail, and put it into tail and update the tail
        for i in range(1, len(l)):
            if l[i] != l[newTail]:
                newTail += 1
                l[newTail] = l[i]
        return newTail + 1
