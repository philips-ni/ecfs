"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x:x.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        return res
    
    def merge2(self, inters):
        if len(inters) < 2:
            return inters
        merged = [inters[0]]
        self._merge(inters, 1, merged)
        return merged
        
    def _merge(self,inters, idx, merged):
        if idx == len(inters):
            return

        s = inters[idx].start
        e = inters[idx].end
        sM = merged[-1].start
        eM = merged[-1].end
        if e < eM:
            pass
        elif s > eM:
            merged.append(inters[idx])
        else:
            merged[-1].end = e
        self._merge(inters, idx+1, merged)            
        
