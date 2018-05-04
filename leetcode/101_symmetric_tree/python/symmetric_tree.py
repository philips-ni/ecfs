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
    def recur_left(self, root):
        result = []
        if root is None:
            result.append('x')
            return result
        result.append(root.val)
        result += self.recur_left(root.left)
        result += self.recur_left(root.right)
        return result
    def recur_right(self, root):
        result = []
        if root is None:
            result.append('x')
            return result
        result.append(root.val)
        result += self.recur_right(root.right)
        result += self.recur_right(root.left)
        return result
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        l = self.recur_left(root)
        r = self.recur_right(root)
        # print l
        # print r
        return l == r
