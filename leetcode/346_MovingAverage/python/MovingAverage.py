class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.window.append(val)
        else:
            self.window.pop(0)
            self.window.append(val)
        return sum(self.window) // len(self.window)
        
from collections import deque
class MovingAverage1(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = deque()
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.window.append(val)
        else:
            self.window.popleft()
            self.window.append(val)
        return sum(self.window) // len(self.window)
        
