import collections
class Solution(object):
    def firstUniqChar(self, s):
        # to keep the el->occurence mapping
        d1 = collections.defaultdict(int)
        # to keep the el->first occurence idx mapping
        d2 = {}
        for i, el in enumerate(s):
            d1[el] += 1
            if el not in d2:
                d2[el] = i
        uniqChars = [el for el in d1 if d1[el] == 1]
        if len(uniqChars) == 0:
            return -1
        ret = float("inf")
        for el in uniqChars:
            ret = min(ret, d2[el])
        return ret
        
        
