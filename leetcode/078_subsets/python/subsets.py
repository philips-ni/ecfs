
class Solution(object):
    def subsets(self,l):
        length = len(l)
        sets = []
        for i in range(0, pow(2,length)):
            s = []
            for j in range(0, length):
                # if the No. j bit is 1
                if (i & (1 << j)) > 0 :
                    s.append(l[j])
            sets.append(s)
        return sets
        
    def subsets(self, l):
        # print "l: " + str(l)
        if len(l) == 0:
            return [[]]
        elif len(l) == 1:
            return [l, []]

        return self.merge(self.subsets(l[:-1]), l[-1])

    def merge(self, sets, el):
        # print "sets: " + str(sets)
        mergedSets = sets[:]
        for s in sets:
            ts = s[:]
            ts.append(el)
            mergedSets.append(ts)
        return mergedSets
        
