import unittest
import add2num

class TestAdd2Num(unittest.TestCase):

    def test_addTwoNumbers(self):
        s = add2num.Solution()
        l1n1 = add2num.ListNode(2)
        l1n2 = add2num.ListNode(4)
        l1n3 = add2num.ListNode(3)
        l1n1.next = l1n2
        l1n2.next=l1n3

        l2n1 = add2num.ListNode(5)
        l2n2 = add2num.ListNode(6)
        l2n3 = add2num.ListNode(4)
        l2n1.next = l2n2
        l2n2.next = l2n3
        
        result = s.addTwoNumbers(l1n1,l2n1)
        s.dumpList(result)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)


    def test_addTwoNumbers2(self):
        s = add2num.Solution()
        l1n1 = add2num.ListNode(2)
        l1n2 = add2num.ListNode(4)
        l1n3 = add2num.ListNode(3)
        l1n4 = add2num.ListNode(9)
        l1n1.next = l1n2
        l1n2.next=l1n3
        l1n3.next=l1n4

        l2n1 = add2num.ListNode(5)
        l2n2 = add2num.ListNode(6)
        l2n3 = add2num.ListNode(4)
        l2n1.next = l2n2
        l2n2.next = l2n3
        
        result = s.addTwoNumbers(l1n1,l2n1)
        s.dumpList(result)
        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
        self.assertEqual(result.next.next.next.val, 9)
        
if __name__ == '__main__':
    unittest.main()
