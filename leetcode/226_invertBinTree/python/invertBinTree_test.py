
import unittest
import invertBinTree

class TestInvertbintree(unittest.TestCase):
    def test_invertTree(self):
        s = invertBinTree.Solution()
        tree1 = invertBinTree.setupTree([4,2,7,1,3,6,9])
        tree1 = s.invertTree(tree1)
        self.assertEqual(tree1.convertTreeToList(), [4,7,2,9,6,3,1])
if __name__ == '__main__':
    unittest.main()
