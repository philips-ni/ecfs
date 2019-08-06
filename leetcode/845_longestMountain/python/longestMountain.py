class Solution(object):
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0
        while base < N:
            # print("base: {}".format(base))
            end = base
            if end + 1 < N and A[end] < A[end + 1]:
                while end + 1 < N and A[end] < A[end + 1]:
                    end += 1
                if end + 1 < N and A[end] > A[end + 1]:
                    while end + 1 < N and A[end] > A[end + 1]:
                        end += 1
                        ans = max(ans, end - base + 1)
            # print("end: {}".format(end))                        
            base = max(end, base + 1)
        return ans
