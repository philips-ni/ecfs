import collections
class Solution(object):
    def canPermutePalindrome(self,s):
        count = collections.Counter(s)
        odd_counter = 0
        ret = True
        for key in count.keys():
            if count[key] % 2 != 0:
                odd_counter += 1
                if odd_counter > 1:
                    ret = False
                    break
        return ret
                
            
