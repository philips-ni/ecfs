import unittest
import removeNthFromEnd

class TestRemoventhfromend(unittest.TestCase):
    def test_removeNthFromEnd(self):
        s = removeNthFromEnd.Solution()
        elements = [1,2,3]
        head = removeNthFromEnd.initList(elements)
        removeNthFromEnd.dump(head)
        head = s.removeNthFromEnd(head,3)
        removeNthFromEnd.dump(head)
        
if __name__ == '__main__':
    unittest.main()
