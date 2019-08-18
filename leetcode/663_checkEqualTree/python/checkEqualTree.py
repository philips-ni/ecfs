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
    def checkEqualTree(self, root):
        # Seen will store each subree's sum, and if found one of them is half of total then we found it
        seen = []
        def sum_(node):
            if not node: return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen
