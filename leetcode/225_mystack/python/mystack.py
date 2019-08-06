from collections import deque
class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return  not self.stack
