from collections import defaultdict,Counter
class Solution(object):
   def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lookup = Counter(s)
        for c in lookup:
            if lookup[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
