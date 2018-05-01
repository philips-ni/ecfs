"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, l):
        if len(l) == 0:
            return [[]]
        elif len(l) == 1:
            return [l, []]
        l.sort()
        return self.merge(self.subsetsWithDup(l[:-1]), l[-1])
    
    def merge(self, sets, el):
        mergedSets = sets[:]
        for s in sets:
            ts = s[:]
            ts.append(el)
            ts.sort()
            if ts not in mergedSets:
                mergedSets.append(ts)
        return mergedSets
        
