
import collections

class Solution:
    def checkInclusion(self, s1, s2):
	if len(s1) > len(s2):
	    return False        
	hash_s1 = 0
	hash_s2 = 0
	d = len(s1)
	for i in range(d):
	    hash_s1 += hash(s1[i])
	    hash_s2 += hash(s2[i])
	if hash_s1 == hash_s2:
	    return True
	for i in range(d, len(s2)):
	    hash_s2 += hash(s2[i]) - hash(s2[i - d])
	    if hash_s1 == hash_s2:
                return True
	return False
    
class Solution2(object):
    def checkInclusion(self, s1, s2):
        idx  = 0
        len_s2 = len(s2)
        len_s1 = len(s1)
        ret = False
        while idx + len_s1 <= len(s2):
            if self.isPermutation(s2[idx:idx+len_s1], s1):
                ret = True
                break
            else:
                idx += 1
        return ret
    
    def isPermutation(self, t1, t2):
        def getSign(s):
            d = collections.Counter(s)
            ret = ""
            for k in d:
                ret += "{}{}".format(k, d[k])
            return ret
        
        return getSign(t1) == getSign(t2)
                
