
import unittest
import linked_list_cycle

class TestLinked_List_Cycle(unittest.TestCase):
    def test_hasCycle(self):
        s = linked_list_cycle.Solution()
        node1 = linked_list_cycle.ListNode(1)
        node2 = linked_list_cycle.ListNode(2)
        node3 = linked_list_cycle.ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1
        l1 = node1
        self.assertEqual(s.hasCycle(l1), True)
        l2 = linked_list_cycle.initList([1,2,3,4])
        self.assertEqual(s.hasCycle(l2), False)
        
if __name__ == '__main__':
    unittest.main()
