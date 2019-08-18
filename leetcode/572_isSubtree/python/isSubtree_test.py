
import unittest
import isSubtree

class TestIssubtree(unittest.TestCase):
    def test_isSubtree(self):
        s = isSubtree.Solution()
        tree1 = isSubtree.setupTree([3,4,5,1,2])
        tree2 = isSubtree.setupTree([4,1,2])
        self.assertEqual(s.isSubtree(tree1, tree2), True)

        tree1 = isSubtree.setupTree([3,4,5,1,2, None, None, None, None, 0])
        self.assertEqual(s.isSubtree(tree1, tree2), False)
        tree1 = isSubtree.setupTree([3,4,5,1,2, 2,3])
        self.assertEqual(s.isSubtree(tree1, tree2), True)        
        
if __name__ == '__main__':
    unittest.main()
