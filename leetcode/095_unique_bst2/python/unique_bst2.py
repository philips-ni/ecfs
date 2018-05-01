from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    visited = []
    _inorderTraversal(root,visited)
    print visited
    return visited

def _inorderTraversal(root,visited):
    if root == None:
        return
    _inorderTraversal(root.left, visited)
    if root.val:
        visited.append(root.val)
    _inorderTraversal(root.right,visited)            

def layeredTraversal(root):
    visited = []
    q = deque([], 100)
    if root is None:
        return []
    q.append(root)
    while q:
        currentNode = q.popleft()
        if currentNode == None:
            visited.append(None)
        else:
            visited.append(currentNode.val)
            q.append(currentNode.left)
            q.append(currentNode.right)
    print visited
    return visited
        
    
    
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def helper(vals):
            if not vals:
                return [None]
            if len(vals) == 1:
                return [TreeNode(vals[0])]
            nodeList = []
            for i in range(len(vals)):
                leftArr = helper(vals[0:i])
                rightArr = helper(vals[i+1:])
                for l in leftArr:
                    for r in rightArr:
                        node = TreeNode(vals[i])
                        node.left = l
                        node.right = r
                        nodeList.append(node)
            return nodeList
        if n == 0:
            return []
        vals = [i for i in range(1,n+1)]
        return helper(vals)
