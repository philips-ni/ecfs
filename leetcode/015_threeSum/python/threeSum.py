"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nlist):
        ret = []        
        if len(nlist) < 3:
            return ret
        nlist.sort()
        for i in range(0, len(nlist) - 2):
            if i > 0 and nlist[i] == nlist[i-1]:
                continue
            j = i + 1
            k = len(nlist) - 1
            while j < k:
                if nlist[i] + nlist[j] + nlist[k] > 0:
                    k -= 1
                elif nlist[i] + nlist[j] + nlist[k] < 0:
                    j += 1
                else:
                    ret.append([nlist[i],nlist[j],nlist[k]])
                    while j < k and nlist[j] == nlist[j+1]:
                        j += 1
                    while k > j and nlist[k] == nlist[k-1]:
                        k -= 1                        
                    j += 1
                    k -= 1
        return ret

