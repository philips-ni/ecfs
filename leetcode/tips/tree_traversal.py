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
            while parentNode == None:
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
    # Base CAse 
    if root is None:
        return
     # create an empty stack and push root to it
    stack = []
    stack.append(root)
    #  Pop all items one by one. Do following for every popped item
    #   a) print it
    #   b) push its right child
    #   c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while(len(stack) > 0):
         # Pop the top item from stack and print it
        current = stack.pop()
        print current.val
        # Push right and left children of the popped node
        # to stack
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

def print_tree_in(root):
    """
    1) Create an empty stack S.
    2) Initialize current node as root
    3) Push the current node to S and set current = current->left until current is NULL
    4) If current is NULL and stack is not empty then 
    a) Pop the top item from stack.
    b) Print the popped item, set current = popped_item->right 
    c) Go to step 3.
    5) If current is NULL and stack is empty then we are done.
    """
    stack = []
    current = root
    done = False
    while not done:
        if current is not None:
            stack.append(current)
            current = current.getLeft();
        else:
            if len(stack) > 0:
                current = stack.pop()
                print current.getValue()
                current = current.getRight()
            else:
                done = True

def print_tree_post(root): 
    if root is None:
        return         
     
    # Create two stacks 
    s1 = []
    s2 = []
     
    # Push root to first stack
    s1.append(root)
     
    # Run while first stack is not empty
    while (len(s1) >0):
         
        # Pop an item from s1 and append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of removed item to s1
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None :
            s1.append(node.right)
 
        # Print all eleements of second stack
    while(len(s2) > 0):
        node = s2.pop()
        print node.val,
 
 
def print_tree_post1(root):
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
print_tree_in(root)

"""
print_tree_pre(root)
print "-" * 10
print_tree_pre_r(root)
print "-" * 10
print_tree_in(root)
print "-" * 10
print_tree_post(root)
"""
