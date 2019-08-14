class Solution:
    def minIncrementForUnique(self, A):
        if not A: return 0
        A.sort()
        size = len(A)
        i = 1
	count = 0
	max_seen = A[0]
        while i < size:
            if A[i] <= max_seen:
                k = max_seen - A[i] + 1
                A[i] += k
                count += k
            max_seen = A[i]
            i += 1
        return count
    
class Solution1:
    def minIncrementForUnique(self, A):
        if not A:
            return 0
        A = sorted(A)
        # print(A)
        # start means the least unique number of A[i]
        start = A[0] + 1
        ans = 0
        
        for i in range(1, len(A)):
            # if A[i] > start, then the next unique number is at least A[i] + 1
            if A[i] > start:
                start = A[i] + 1
            # if A[i] is equal to the least unique number, simply add 1 to start
            elif A[i] == start:
                start += 1
            # if A[i] is less than the least unique number, A[i] needs to add at least (start - A[i]) to become unique
            else:
                ans += start - A[i]
                start += 1
            # print("i: {}, start: {}, ans: {}".format(i, start, ans))                
        return ans
