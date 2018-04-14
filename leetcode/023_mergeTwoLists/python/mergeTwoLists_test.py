
import unittest
import mergeTwoLists

class TestMergetwolists(unittest.TestCase):
    def test_mergeTwoLists(self):
        s = mergeTwoLists.Solution()
        l1 = mergeTwoLists.initList([1,2,4])
        l2 = mergeTwoLists.initList([1,3,4])
        mergedL = s.mergeTwoLists(l1,l2)
        mergeTwoLists.dump(mergedL)
        
if __name__ == '__main__':
    unittest.main()
