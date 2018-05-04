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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m >= n:
            return head
        prev_node = None
        curr_node = head
        for i in range(1, m): # iterating over linked list to find m-node
            prev_node = curr_node
            curr_node = curr_node.next
            if curr_node is None:
                return head
        before_m_node = prev_node
        m_node = curr_node # remember M-node
        next_node = curr_node.next  # Remember next node
        for i in range(m, n):
            prev_node = curr_node
            curr_node = next_node  # Move to next node.
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE!
        m_node.next = next_node # redirecting M-node to ex-N+1 node
        if before_m_node:
            before_m_node.next = curr_node # redirecting M-1 node to N-node
        else:
            head = curr_node
        return head
