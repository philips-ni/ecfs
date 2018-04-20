
class Solution(object):
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
        
