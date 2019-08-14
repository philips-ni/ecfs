from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def convertTreeToList(self):
        root = self
        retL = []
        if root is None: 
            return
        # Create an empty queue for level order traversal 
        queue = [] 
        # Enqueue Root and initialize height 
        queue.append(root) 
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue
            retL.append(queue[0].val)
            node = queue.pop(0) 
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right)
        return retL

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
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if root == None:
                return 0, None
            l_depth, l_lca = helper(root.left)
            r_depth, r_lca = helper(root.right)
            depth = max(l_depth, r_depth) + 1
            if l_depth == r_depth:
                lca = root
            elif l_depth > r_depth:
                lca = l_lca
            else:
                lca = r_lca
            return depth, lca
        _, lca = helper(root)
        return lca
