import collections
class Solution(object):
    def numEquivDominoPairs(self,dominoes):
        def sign(l):
            sign = 0
            for el in l[::-1]:
                sign = sign * 10 + el
            return sign
        d_dict = collections.defaultdict(int)
        ret = 0
        for d in dominoes:
            item = sign(sorted(d))
            d_dict[item] += 1
        for v in d_dict.values():
            if v > 1:
                ret += v * (v-1) // 2
        return ret
    
