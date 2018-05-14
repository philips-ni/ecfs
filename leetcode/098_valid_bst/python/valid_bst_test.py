
import unittest
import valid_bst

class TestValid_Bst(unittest.TestCase):
    def test_isValidBST(self):
        s = valid_bst.Solution()

        root = valid_bst.setupTree([10,5,15,None,None,6,20])
        valid_bst.layeredTraversal(root)
        self.assertEqual(s.isValidBST(root), False)
        
        root = valid_bst.setupTree([5,1,4,None,None,3,6])
        valid_bst.layeredTraversal(root)
        self.assertEqual(s.isValidBST(root), False)
        
if __name__ == '__main__':
    unittest.main()
