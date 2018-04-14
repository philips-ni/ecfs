
class Solution(object):
    def strStr(self, s, subS):
        slen = len(s)
        sslen = len(subS)

        if slen < sslen:
            return -1

        if s == subS:
            return 0

        sIdx = 0
        while sIdx < slen - sslen + 1:
            ssIdx = 0
            # print "sIdx : %d" % sIdx
            tIdx = sIdx
            while ssIdx < sslen:
                # print "ssIdx : %d" % ssIdx
                if s[tIdx] == subS[ssIdx]:
                    # print "tIdx : %d" % tIdx
                    ssIdx += 1
                    tIdx += 1
                else:
                    break
            if ssIdx == sslen:
                return sIdx
            sIdx += 1
        return -1
        
