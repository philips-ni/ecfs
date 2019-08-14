
import unittest
import lcaDeepestLeaves

class TestLcadeepestleaves(unittest.TestCase):
    def test_lcaDeepestLeaves(self):
        s = lcaDeepestLeaves.Solution()
        tree1 = lcaDeepestLeaves.setupTree([1,2,3])
        subT = s.lcaDeepestLeaves(tree1)
        self.assertEqual(subT.convertTreeToList(), [1,2,3])

        tree1 = lcaDeepestLeaves.setupTree([1,2,3,4])
        subT = s.lcaDeepestLeaves(tree1)
        self.assertEqual(subT.convertTreeToList(), [4])

        tree1 = lcaDeepestLeaves.setupTree([1,2,3,4,5])
        subT = s.lcaDeepestLeaves(tree1)
        self.assertEqual(subT.convertTreeToList(), [2, 4, 5])
        
#         self.assertEqual(tree1.convertTreeToList(), [1,2,3,4,5])
#        

#        tree1 = lcaDeepestLeaves.setupTree([1,2,3,4])
#        self.assertEqual(s.lcaDeepestLeaves(tree1), [4])
#        tree1 = lcaDeepestLeaves.setupTree([1,2,3,4,5])
#        self.assertEqual(s.lcaDeepestLeaves(tree1), [2,4,5])
#


if __name__ == '__main__':
    unittest.main()
