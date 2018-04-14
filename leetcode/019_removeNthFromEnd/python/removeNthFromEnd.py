# Definition for singly-linked list.
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
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        firstPointer = head
        secondPointer = firstPointer
        outOfRange = False
        for i in range(0, n - 1):
            if secondPointer.next:
                secondPointer = secondPointer.next
            else:
                outOfRange = True
                
        if outOfRange:
            return head

        if secondPointer.next == None:
            head = firstPointer.next
            return head
        
        prevFirst = None
        while secondPointer.next:
            prevFirst = firstPointer
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        prevFirst.next = prevFirst.next.next
        return head
        
        
