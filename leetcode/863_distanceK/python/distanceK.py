import collections
"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
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
        if l[idx] is not None:
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
    def findNode(self, root, target):
        if root is None:
            return None,None
        if root.val == target:
            return root
        ret = self.findNode(root.left,target)
        if ret is not None:
            return ret
        else:
            return self.findNode(root.right, target)
    
    def distanceK(self, root, target, K):
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        targetNode = self.findNode(root,target)
        queue = collections.deque([(targetNode, 0)])
        visited = [targetNode]
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visited:
                    visited.append(nei)
                    queue.append((nei, d+1))
        return []
