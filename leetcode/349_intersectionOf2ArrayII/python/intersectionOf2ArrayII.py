from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        counterN1 = Counter(nums1)
        counterN2 = Counter(nums2)
        if len(counterN1.keys()) > len(counterN2.keys()):
            counterN1, counterN2 = counterN2, counterN1
        common_els = []
        for k in counterN1:
            if k in counterN2.keys():
                common_els.append(k)
        ret = []
        for el in common_els:
            ret.extend([el for _ in range(min(counterN1[el], counterN2[el]))])
        return ret
