from collections import defaultdict
class Solution1(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        value_idx_dict = defaultdict(list)
        for i,n in enumerate(nums1):
            value_idx_dict[n].append(("nums1",i))
        for i,n in enumerate(nums2):
            value_idx_dict[n].append(("nums2",i))
        
        ret = self.maxNumberHelper(nums1,nums2,value_idx_dict,k)
        return self.reorg(ret, value_idx_dict)

    def maxNumberHelper(self,nums1,nums2,value_idx_dict,k):
        ret = []
        if k == 1:
            max_val = max(nums1 + nums2)
            if max_val in nums:
                nums1.remove(max_val)
            else:
                nums2.remove(max_val)
            ret.append(max_val)
            return ret
        else:
            ret_tmp = self.maxNumberHelper(nums1,nums2,value_idx_dict,k-1)
            ret_last_one = self.maxNumberHelper(nums1,nums2,value_idx_dict,1)
            while not self.isValid(ret_tmp,ret_last_one,value_idx_dict):
                ret_last_one = self.maxNumberHelper(nums1,nums2,value_idx_dict,1)
            ret = ret_tmp + ret_last_one
        return ret

    
    
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret
    
    
    def mergeMax(self, nums1, nums2):
        print("starint merge " + str(nums1) + "  "  + str(nums2))
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        print("output: " + str(ans))
        return ans
    
    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n : return ret
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret
    
