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
        
            
class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        current = root
        visited = []
        done = False
        while not done:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack 
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left 
                # BackTrack from the empty subtree and visit the Node
                # at the top of the stack; however, if the stack is 
                # empty you are done
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    visited.append(current.val)
                    # We have visited the node and its left 
                    # subtree. Now, it's right subtree's turn
                    current = current.right 
                else:
                    done = 1        
        return visited
    
    def inorderTraversal2(self, root):
        visited = []
        self._inorderTraversal(root,visited)
        return visited
    
    def _inorderTraversal(self, root,visited):
        if root == None:
            return
        self._inorderTraversal(root.left, visited)
        if root.val:
            visited.append(root.val)
        self._inorderTraversal(root.right,visited)            
