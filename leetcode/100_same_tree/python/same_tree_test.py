
import unittest
import same_tree

class TestSame_Tree(unittest.TestCase):
    def test_isSameTree(self):
        s = same_tree.Solution()
        tree1 = same_tree.setupTree([10,5,15,None,None,6,20])
        tree2 = same_tree.setupTree([10,5,15,None,None,6,20])                
        self.assertEqual(s.isSameTree(tree1, tree2), True)

        tree1 = same_tree.setupTree([1,2,3])
        tree2 = same_tree.setupTree([1,2,3])
        self.assertEqual(s.isSameTree(tree1, tree2), True)

        tree1 = same_tree.setupTree([1,2])
        tree2 = same_tree.setupTree([1,None,2])        
        self.assertEqual(s.isSameTree(tree1, tree2), False)
        
        tree1 = same_tree.setupTree([1,2,1])
        tree2 = same_tree.setupTree([1,1,2])
        self.assertEqual(s.isSameTree(tree1, tree2), False)
        
if __name__ == '__main__':
    unittest.main()
