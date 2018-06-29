
import unittest
import isBalancedBinTree

class TestIsbalancedbintree(unittest.TestCase):
    def test_isBalanced(self):
        s = isBalancedBinTree.Solution()
        tree1 = isBalancedBinTree.setupTree([3,9,20,None,None,15,7])
        self.assertEqual(s.isBalanced(tree1), True)
        
if __name__ == '__main__':
    unittest.main()
