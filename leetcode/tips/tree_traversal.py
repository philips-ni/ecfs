from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def getValue(self):
        return self.val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
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

def print_tree_pre_r(root):
    if root is None:
        return
    print root.getValue()
    print_tree_pre_r(root.getLeft())
    print_tree_pre_r(root.getRight())

def print_tree_pre(root):
    stack = []
    current = root
    while True:
        while current is not None:
            print current.getValue()
            stack.append(current)
            current = current.getLeft();
        if not stack:
            return
        current = stack.pop()
        while current.getRight is None and stack:
            current = stack.pop()
        current = current.getRight();  

def print_tree_in(root):
    stack = []
    current = root
    while True:
        while current is not None:
            stack.append(current)
            current = current.getLeft();
        if not stack:
            return
        current = stack.pop()
        print current.getValue()
        while current.getRight is None and stack:
            current = stack.pop()
            print current.getValue()
        current = current.getRight(); 
 
def print_tree_post(root):
    stack = []
    current = root
    while True:
        while current is not None:
            stack.append((current,False))
            current = current.getLeft();
        if stack:
            current, visited = stack.pop()
        else:
            return 
        while((current.getRight() is None) or (visited is True)) and stack:
            print current.getValue()
            current, visited = stack.pop()
        else:
            if not stack and visited:
                print current.getValue()
                return
            stack.append((current,True))
            current = current.getRight();

            
root = setupTree([3,9,20,None,None,15,7])
print_tree_pre(root)
print "-" * 10
print_tree_pre_r(root)
print "-" * 10
print_tree_in(root)
print "-" * 10
print_tree_post(root)
