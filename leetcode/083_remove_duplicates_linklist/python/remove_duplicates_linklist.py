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
        prevNode = head
        currNode = head.next
        while currNode != None:
            if currNode.val == prevNode.val:
                currNode = currNode.next
                prevNode.next = currNode
            else:
                prevNode = currNode
                currNode = currNode.next
        return head

