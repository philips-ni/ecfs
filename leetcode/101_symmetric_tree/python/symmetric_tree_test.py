import unittest
import symmetric_tree

class TestSymmetric_Tree(unittest.TestCase):
    def test_isSymmetric(self):
        s = symmetric_tree.Solution()
        tree1 = symmetric_tree.setupTree([1,2,2,3,4,4,3])
        self.assertEqual(s.isSymmetric(tree1), True)
        tree2 = symmetric_tree.setupTree([1,2,2,None,3,None,3])
        self.assertEqual(s.isSymmetric(tree2), False)

        tree3 = symmetric_tree.setupTree([1,2,3,3,None,2,None])
        self.assertEqual(s.isSymmetric(tree3), False)
        
        
if __name__ == '__main__':
    unittest.main()
