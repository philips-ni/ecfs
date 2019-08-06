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
        print "Empty list"
        return
    iter = head
    while iter.next:
        print "%s ->" % iter.val
        iter = iter.next
    print "%s" % iter.val

class Solution(object):
    def reorderList(self, head):
        if head is None: return
        h = head
        curr = head
        stack = []
        count = 0
        
	while curr:
            count+=1
            stack.append(curr)
            curr = curr.next
        while count>1:
            temp = h.next
            h.next = stack.pop()
            h.next.next = temp
            count-=2
            h = h.next.next
        h.next = None
