class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        # Link to video https://www.youtube.com/watch?v=uufaK2uLnSI
        """
				
				
        l = 0
        r = len(nums)-1
        
        while (l <= r):
            mid = (l+r)/2
            # case 1:
            if nums[mid] == target:
                return mid
            
            #case  2: (sorted right)
            if nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            
            #case 3: (sorted left)
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        
        return -1
