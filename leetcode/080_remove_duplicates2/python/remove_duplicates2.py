
class Solution(object):
    def removeDuplicates(self, l):
        length = len(l)
        if length < 3:
            return length
        prevC = l[0]
        idx = 1
        prevCounter = 1
        removedCounter = 0
        while idx < length - removedCounter:
            # print "idx: %d, prevCounter: %d" % (idx, prevCounter)
            if l[idx] == prevC:
                # print "idx: %d, prevCounter: %d" % (idx, prevCounter)
                if prevCounter == 2:
                    # print "delete l[%d], %d " % (idx, l[idx])
                    del l[idx]
                    removedCounter += 1
                else:
                    prevCounter += 1
                    idx += 1
            else:
                prevC = l[idx]
                prevCounter = 1
                idx += 1
        return idx
        

