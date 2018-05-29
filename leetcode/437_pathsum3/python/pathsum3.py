"""

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
"""
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def setupTree(l):
    if len(l) == 0:
        return None
    root = TreeNode(l[0])
    isLeft = True
    idx = 1
    q = deque([], 100)
    parentNode = root
    while idx < len(l):
        if l[idx]:
            currNode = TreeNode(l[idx])
        else:
            currNode = None
        q.append(currNode)
        if isLeft:
            parentNode.left = currNode
            isLeft = False
        else:
            parentNode.right = currNode
            parentNode = q.popleft()
            if parentNode == None:
                parentNode = q.popleft()
            isLeft = True                
        idx += 1
    return root

class Solution(object):
    def pathSum(self, root, sum):
        if root is  None:
            return 0
        else:
            return self.sumUp(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def sumUp(self, root, pre, sum):
        if root is None:
            return 0
        else:
            current = root.val + pre
            ret = self.sumUp(root.left, current, sum) + self.sumUp(root.right, current, sum)
            if current == sum:
                ret += 1
            return ret

        
