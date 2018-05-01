
import unittest
import unique_bst2

class TestUnique_Bst2(unittest.TestCase):
    def test_generateTrees(self):
        s = unique_bst2.Solution()
        trees = s.generateTrees(4)
        for tree in trees:
            unique_bst2.layeredTraversal(tree)
if __name__ == '__main__':
    unittest.main()
