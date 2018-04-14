import unittest
import revertLinkList

class TestRevertlinklist(unittest.TestCase):
    def test_revertLinkList(self):
        s = revertLinkList.Solution()
        l1 = revertLinkList.initList([1,2,4,5])
        l2 = s.revertLinkList(l1)
        revertLinkList.dump(l2)
        l1 = revertLinkList.initList([1])
        l2 = s.revertLinkList(l1)
        revertLinkList.dump(l2)
        
if __name__ == '__main__':
    unittest.main()
