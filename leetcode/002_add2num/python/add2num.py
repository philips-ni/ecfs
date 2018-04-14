"""
Summary: add2num
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersImpl(l1,l2,0)

    def addTwoNumbersImpl(self, l1, l2, carry):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type carry: int
        :rtype: ListNode
        """
        result = ListNode(0)
        if l1 == None and l2 != None:
            if carry > 0:
                tmpNode = ListNode(carry)
                return self.addTwoNumbersImpl(tmpNode,l2,0)
            else:
                return l2

        if l1 != None and l2 == None:
            if carry > 0:
                tmpNode = ListNode(carry)
                return self.addTwoNumbersImpl(l1,tmpNode,0)
            else:
                return l1

        if l1 == None and l2 == None:
            if carry > 0:
                tmpNode = ListNode(carry)
                return tmpNode
            else:
                return None
            
        l1Next = l1.next
        l2Next = l2.next

        sumOfHead = l1.val + l2.val + carry
        # print "%d + %d = %d" % (l1.val, l2.val, sumOfHead)        
        if sumOfHead < 10:
            result.val = sumOfHead
            result.next = self.addTwoNumbersImpl(l1Next, l2Next,0)
        else:
            result.val = sumOfHead - 10
            result.next = self.addTwoNumbersImpl(l1Next, l2Next,1)
        return result

    def dumpList(self,l):
        out = []
        while l != None:
            out.append(l.val)
            l = l.next
        print out
        
    
