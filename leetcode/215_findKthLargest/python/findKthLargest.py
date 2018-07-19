class Solution0(object):
    def findKthLargest(self, l, k):
        sorted_first_k_nums = l[0:k]
        sorted_first_k_nums.sort()
        for i in range(k,len(l)):
            if l[i] > sorted_first_k_nums[0]:
                sorted_first_k_nums[0] = l[i]
                sorted_first_k_nums.sort()
        return sorted_first_k_nums[0]
    
import heapq
class Solution01(object):
    def findKthLargest(self, l, k):
        return heapq.nlargest(k,l)[-1]

import heapq
class Solution(object):
    def findKthLargest(self, l, k):
        if k > len(l):
            raise ValueError("%d is bigger than list's length" % k)
        firstKthLagest = l[:k]
        heapq.heapify(firstKthLagest)
        for i in range(k, len(l)):
            if l[i] > firstKthLagest[0]:
                heapq.heappop(firstKthLagest)
                heapq.heappush(firstKthLagest, l[i])
        return firstKthLagest[0]
        
        
