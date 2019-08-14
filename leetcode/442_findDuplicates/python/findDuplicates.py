class Solution(object):
    def findDuplicates(self,nums):
        # O(n) time complexity
        # O(1) space complexity
        # credit to Wayne-x (I had to peek at his solution)
        # two conditions are very important
        output = []
        for num in nums:
            # this is based  1 <= a[i] <= n
            if nums[abs(num)-1] < 0:
                # second time see nums[abs(num)-1], found the duplicated
                output.append(abs(num))
            else:
                # first time see nums[abs(num)-1], convert it to negative
                nums[abs(num)-1] *= -1
            # print(nums)
        return output
    
