
import unittest
import unique_bst

class TestUnique_Bst(unittest.TestCase):
    def test_numTrees(self):
        s = unique_bst.Solution()
        self.assertEqual(s.numTrees(1), 1)
        self.assertEqual(s.numTrees(2), 2)
        self.assertEqual(s.numTrees(3), 5)
        self.assertEqual(s.numTrees(4), 14)
        
        
if __name__ == '__main__':
    unittest.main()
