from collections import deque
# Definition for a binary tree node.
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
    # print visited
    return visited

class Solution(object):
    def isValidBST(self, root):
        if root is None:
            return True

        left = root.left
        right = root.right

        if left == None and right == None:
            return True
        
        if not self.allNodesLess(left, root.val)  or not self.allNodesGreater(right, root.val):
            return False
        
        return self.isValidBST(left) and self.isValidBST(right)

    def allNodesLess(self, root, val):
        nodes = layeredTraversal(root)
        for node in nodes:
            if node is not None and node >= val:
                return False
        return True

    def allNodesGreater(self, root, val):
        nodes = layeredTraversal(root)
        for node in nodes:
            if node is not None and node <= val:
                return False
        return True
    

