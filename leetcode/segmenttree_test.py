class SegmentTreeNode(object):
  def __init__(self,start, end):
      self.start = start
      self.end = end
      self.min = 0
      self.left = None
      self.right = None
      
class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
    
    def createTree(self,l, r):
        if(l > r):
            return None
        if(l==r):
            obj = SegmentTreeNode(l,r)
            obj.min = self.nums[l]
            return obj
  
        node = SegmentTreeNode(l,r)
    
        mid = (l+r) // 2
        mid = int(mid)
        node.left = self.createTree(l,mid)
        node.right = self.createTree(mid+1,r)
        node.min = min(node.left.min, node.right.min)
        return node
  
  
    def printTree(_self, root):
        level = [root]
        raws = []
        while(len(level) > 0):
            nextLevel = []
            count = 0
            maxCount = 0
            numsStr = ""
            for nodes in level : 
                numsStr = numsStr + "      " + str(nodes.min)
                count = count +1
                if nodes.left is not None  : nextLevel.append(nodes.left)
                if nodes.right is not None : nextLevel.append(nodes.right)
            raws.append([count,numsStr])
            if count > maxCount : maxCount = count
            level = nextLevel
        for raw in raws :
            count = raw[0]
            count = int((maxCount-count)/2)
            print ((" " * (count+2)) + raw[1])
      

nums = [18, 17, 13, 19, 15, 11, 20]
sg = SegmentTree(nums)
root = sg.createTree(0,(len(nums)-1))
sg.printTree(root)   
