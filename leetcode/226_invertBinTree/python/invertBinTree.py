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

class Solution1(object):
    def invertTree(self, root):
        if root == None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root
        


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
