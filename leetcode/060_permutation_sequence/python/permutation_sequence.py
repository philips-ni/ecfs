"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

The idea is as follow:

For permutations of n, the first (n-1)! permutations start with 1, next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number, ...

take n = 3 as an example, the first 2 (that is, (3-1)! ) permutations start with 1, next 2 start with 2 and last 2 start with 3. For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2, which is the smallest remaining number (2 and 3). So we can use a loop to check the region that the sequence number falls in and get the starting digit. Then we adjust the sequence number and continue
"""
class Solution(object):
    def getPermutation(self, n, k):
        facts = [1,1]
        for i in range(2, n+1):
            facts.append(facts[-1] * i)
        nums = range(1, n+1)
        return self._getPermutation(facts, nums, n, k)

    def _getPermutation(self, facts, nums, n, k):
        if k == 1:
            return self.convertToStr(nums)
        divN  = k / facts[n-1]
        reminder = k % facts[n-1]
        if reminder == 0:
            firstN = nums[divN - 1]
            nums.remove(firstN)
            return str(firstN) + self.convertToStr(nums[::-1])
        firstN = nums[divN]
        nums.remove(firstN)
        return str(firstN) + self._getPermutation(facts, nums, n - 1, k - divN * facts[n-1])
    
    def convertToStr(self, nums):
        s = ""
        for n in nums:
            s += str(n)
        return s
        
        
