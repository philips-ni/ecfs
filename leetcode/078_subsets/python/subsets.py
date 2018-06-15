import math
class Solution(object):
    def subsets(self,l):
        length = len(l)
        sets = []
        for i in range(1 << length):
            bit_array = i
            s = []
            while bit_array:
                tmp = bit_array & (bit_array - 1)
                pos = int(math.log(bit_array - tmp, 2))
                s.append(l[pos])
                bit_array = tmp
            sets.append(s)
        return sets
    
    def subsets3(self,l):
        length = len(l)
        sets = []
        for i in range(1 << length):
            s = []
            for j in range(0, length):
                # if the No. j bit is 1
                if (i & (1 << j)) > 0 :
                    s.append(l[j])
            sets.append(s)
        return sets
        
    def subsets2(self, l):
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
        
