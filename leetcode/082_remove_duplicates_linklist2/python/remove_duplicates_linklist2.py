"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
    if head == None:
        print "None"
        return
    iter = head
    while iter.next:
        print "%s ->" % iter.val
        iter = iter.next
    print "%s" % iter.val

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        nextNode = self.deleteDuplicates(head.next)
        if nextNode == None:
            if head.next != None and head.val != head.next.val:
                head.next = nextNode
                return head
            else:
                return None
        elif nextNode.val != head.val and head.next.val == head.val:
            return nextNode
        elif head.val == nextNode.val:
            return nextNode.next
        else:
            head.next = nextNode
            return head
