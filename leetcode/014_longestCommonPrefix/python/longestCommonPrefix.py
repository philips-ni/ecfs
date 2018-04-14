"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, slist):
        if len(slist) == 0:
            return ""
        elif len(slist) == 1:
            return slist[0]

        else:
            s0 = slist[0]
            if len(s0) == 0:
                return ""
            
            foundDiff = False
            for idx in range(0, len(s0)):
                for sIter in slist[1:] :
                    if len(sIter) - 1 < idx or s0[idx] != sIter[idx]:
                        # print "idx : %d" % idx
                        foundDiff = True
                        break
                if foundDiff:
                    break
            if foundDiff:
                return s0[:idx]
            else:
                return s0[:idx+1]
                               
                             
        
        
