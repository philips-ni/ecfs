
class Solution(object):
    def search2(self, nums, targetN):
        if len(nums) == 0:
            return -1
        else:
            return self._search(nums, 0, len(nums) -1, targetN)

    def _search(self,nums, startIdx, endIdx, targetN):
        print "startIdx : %d" % startIdx
        print "endIdx : %d" % endIdx        
        if startIdx == endIdx :
            if nums[startIdx] != targetN:
                return -1
            else:
                return startIdx
        midIdx = (startIdx + endIdx) / 2
        print "midIdx: %d" % midIdx
        if nums[midIdx] == targetN:
            return midIdx
        
        if (nums[midIdx] > nums[startIdx]) :
            if  targetN > nums[startIdx] and targetN < nums[midIdx]:
                return self._search(nums, startIdx, midIdx -1, targetN)
            else:
                return self._search(nums, midIdx + 1, endIdx, targetN)
        else:
            if  targetN > nums[midIdx] and targetN < nums[midIdx]: 
        elif (nums[midIdx] > nums[startIdx]) and  ( targetN > nums[startIdx] and targetN < nums[midIdx]):

        else:

