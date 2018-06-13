
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(list):
    if len(list) == 0:
        return None
    head = ListNode(list[0])
    prevNode = head
    for i in list[1:]:
        currentNode = ListNode(i)
        prevNode.next = currentNode
        prevNode = currentNode
    return head

def dump(head):
    iter = head
    while iter.next:
        print "%s ->" % iter.val
        iter = iter.next
    print "%s" % iter.val

class Solution(object):
    def hasCycle2(self, head):
        fastP = head
        slowP = head
        while fastP and fastP.next:
            fastP = fastP.next.next
            slowP = slowP.next
            if fastP is slowP:
                return True
        return False
    
    def hasCycle(self, head):
        node = head
        from collections import defaultdict        
        visited_dict =  defaultdict(lambda: False)
        while node:
            if visited_dict[id(node)]:
                return True
            else:
                visited_dict[id(node)] = True
            node = node.next
        return False
            
