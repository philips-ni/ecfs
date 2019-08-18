import collections
class MaxQueue:
    def __init__(self):
        self.q_ = collections.deque()
    def push(self, e):
        while self.q_ and e > self.q_[-1]: self.q_.pop()
        self.q_.append(e)
    def pop(self):
        self.q_.popleft()
    def max(self):
        return self.q_[0]
    def __str__(self):
        return str(self.q_)
    

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = MaxQueue()
        ans = []
        for i in range(len(nums)):
            q.push(nums[i])
            if i >= k - 1: 
                ans.append(q.max())
            # in case the current stack top is out of the window
            if nums[i - k + 1] == q.max():
                q.pop()
        return ans
