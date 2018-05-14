class Solution(object):
    def findKthLargest(self, l, k):
        sorted_first_k_nums = l[0:k]
        sorted_first_k_nums.sort()
        for i in range(k,len(l)):
            if l[i] > sorted_first_k_nums[0]:
                sorted_first_k_nums[0] = l[i]
                sorted_first_k_nums.sort()
        return sorted_first_k_nums[0]
