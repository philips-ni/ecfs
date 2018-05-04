
import unittest
import reverse_linkedlist2

class TestReverse_Linkedlist2(unittest.TestCase):
    def test_reverseBetween(self):
        s = reverse_linkedlist2.Solution()
        l1 = reverse_linkedlist2.initList([1,2,3,4,5])
        s.reverseBetween(l1,2,4)
        reverse_linkedlist2.dump(l1)
        
if __name__ == '__main__':
    unittest.main()
