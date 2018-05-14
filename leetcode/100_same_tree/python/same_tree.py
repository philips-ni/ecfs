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
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                if not node1 == node2:
                    return False
        return True
    
    def isSameTree2(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None:
            return False
        if tree2 == None:
            return False

        if tree1.val == tree2.val:
            return self.isSameTree(tree1.left, tree2.left) and \
                self.isSameTree(tree1.right, tree2.right)
        else:
            return False
        
