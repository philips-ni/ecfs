"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution(object):
    def combinationSum3(self,k,n):
        solutions = []
        placed_nums = []
        self.dfs(solutions, placed_nums, k, n)
        return solutions

    def dfs(self, solutions, placed_nums, k, n):
        if len(placed_nums) == k:
            if sum(placed_nums) == n:
                solutions.append(placed_nums)
                return
            else:
                return
        if sum(placed_nums) >= n:
            return
        for i in range(1,10):
            if i not in placed_nums:
                self.dfs(solutions, placed_nums + [i], k, n)
        
        
