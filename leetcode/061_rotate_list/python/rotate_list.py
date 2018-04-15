"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
"""

"""
Solutions:

The idea is :

- Get the length of the list, and do k1 = length % k, so that no matter how big k is, just need rotate k1 times
- Find the oldTail, newTail, newHead,
  - set newTail.next to None,
  - set oldTail.next to head
  - return newHead
"""
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
    def rotateRight(self, head, k):
        length = self.getLength(head)
        if length < 1:
            return head
        k1 = k % length
        if k1 == 0:
            return head
        
        newTail = self.getNode(head, length - k1 -1)
        # print "newTail.val : %d" % newTail.val                
        oldTail = self.getNode(newTail, k1)
        # print "oldTail.val : %d" % oldTail.val
        newHead = newTail.next
        # print "newHead.val : %d" % newHead.val                
        newTail.next = None
        oldTail.next = head
        return newHead
    
    def getLength(self, head):
        length = 0
        iter = head
        while iter:
            length += 1
            iter = iter.next
        # print length
        return length
    
    def getNode(self, head, idx):
        iter = head
        while iter and idx > 0:
            iter = iter.next
            idx -= 1
        return iter
            
        
