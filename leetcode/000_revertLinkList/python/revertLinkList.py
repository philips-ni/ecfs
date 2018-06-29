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
    def revertLinkList2(self, head):
        currentNode = head
        prevNode = None
        nextNode = None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        return prevNode
    
    def revertLinkList(self, head):
        currentNode = head
        while currentNode.next:
            tmpNode = currentNode.next
            currentNode.next = tmpNode.next
            tmpNode.next = head
            head = tmpNode
            # dump(head)
        return head
            
    
