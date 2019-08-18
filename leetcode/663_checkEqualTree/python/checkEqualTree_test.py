
import unittest
import checkEqualTree

class TestCheckequaltree(unittest.TestCase):
    def test_checkEqualTree(self):
        s = checkEqualTree.Solution()
        tree1 = checkEqualTree.setupTree([5, 10,10,None,None,2,3])
        self.assertEqual(s.checkEqualTree(tree1), True)
        tree1 = checkEqualTree.setupTree([1,2,10,None,None,2,20])
        tree1 = checkEqualTree.setupTree([0,-1,1])
        self.assertEqual(s.checkEqualTree(tree1), False)
if __name__ == '__main__':
    unittest.main()
