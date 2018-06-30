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
    q = deque()
    parentNode = root
    for i in l[1:]:
        if i:
            currNode = TreeNode(i)
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
    return root


def check(node):
    if node is None:
        return (0, True)
    l_depth, l_balanced = check(node.left)
    r_depth, r_balanced = check(node.right)
    return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) <= 1

class Solution1:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return check(root)[1]
    
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
