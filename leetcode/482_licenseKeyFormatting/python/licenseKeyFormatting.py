from collections import deque
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S  =  S.replace("-","")
        groups = deque()
        startIdx = 0
        i = len(S)
        while i >= K:
            groups.appendleft(S[i-K:i].upper())
            i -= K
        if i > 0:
            groups.appendleft(S[0:i].upper())
        return "-".join(groups)
