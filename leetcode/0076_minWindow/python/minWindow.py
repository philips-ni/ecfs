"""
Thought process
extend end to right

check whether the condition is satisfied

if satisfied, try to shrink the window by moving start index to right
when satisfied, update the length and result
when not satisfied again -> continue extending end
use a counter for the frequency of characters

use another counter to record how many unique characters have been matched (satisfied the requirements)
"""
import collections
class Solution:
    def minWindow(self, s, t):
        candidates = collections.Counter(t)
        required = len(candidates)
        matched = 0
        counter = collections.Counter()
        min_length = float('inf')
        res = ""
        start = 0
        
        for end, c in enumerate(s):
            if c in candidates:
                counter[c] += 1
                if counter[c] == candidates[c]:
                    matched += 1
            while matched == required:
                if end - start + 1 < min_length:
                    res = s[start:end+1]
                    min_length = end - start + 1
                if s[start] in candidates:
                    counter[s[start]] -= 1
                    if counter[s[start]] < candidates[s[start]]:
                        matched -= 1
                start += 1
        return res
