
import unittest
import inorder_traversal

class TestInorder_Traversal(unittest.TestCase):
    def test_inorderTraversal(self):
        s = inorder_traversal.Solution()

        root = inorder_traversal.setupTree([1,2,3,4,5,6,7])
        self.assertEqual(s.inorderTraversal(root), [4,2,5,1,6,3,7] )
        
        root = inorder_traversal.setupTree([1,None,2,3])
        self.assertEqual(s.inorderTraversal(root), [1,3,2] )

        root = inorder_traversal.setupTree([1,4,2,3])
        self.assertEqual(s.inorderTraversal(root), [3,4,1,2] )

        
if __name__ == '__main__':
    unittest.main()
