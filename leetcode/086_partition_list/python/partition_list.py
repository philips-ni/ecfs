import time
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
    def partition(self, head, x):
        if head == None or head.next == None:
            return head

        # dummy node
        preNode = ListNode(0)
        preNode.next = head 
        nextNode = head

        aPatitionEnd = None
        bPatitionStart = None
        if head.val < x:
            aPatitionStart = head
        else:
            aPatitionStart = None
            
        while nextNode != None:
            # print "preNode:" + str(preNode.val)
            # print "nextNode:" + str(nextNode.val)
            if nextNode.val >= x :
                if bPatitionStart == None:
                    bPatitionStart = nextNode
                    aPatitionEnd = preNode
                    preNode = nextNode
                    nextNode = nextNode.next                    
                else:
                    preNode = nextNode
                    nextNode = nextNode.next                    
            else:
                if aPatitionStart == None:
                    aPatitionStart = nextNode
                if bPatitionStart == None:
                    preNode = nextNode                    
                    nextNode = nextNode.next
                else:
                    preNode.next = nextNode.next
                    aPatitionEnd.next = nextNode
                    aPatitionEnd = nextNode
                    nextNode.next = bPatitionStart
                    nextNode = preNode.next
        if aPatitionStart == None:
            return head
        else:
            return aPatitionStart
