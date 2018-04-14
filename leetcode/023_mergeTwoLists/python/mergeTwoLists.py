
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
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        mergedLHead = None
        if l1.val < l2.val:
            mergedLHead = l1
            mergedLHead.next = self.mergeTwoLists(l1.next, l2)
        else:
            mergedLHead = l2            
            mergedLHead.next = self.mergeTwoLists(l1, l2.next)
        return mergedLHead
        
