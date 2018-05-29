
import unittest
import pathsum3


class TestPathsum3(unittest.TestCase):
    def test_pathSum(self):
        s = pathsum3.Solution()
        tree1 = pathsum3.setupTree([10,5,-3,3,2,None,11,3,-2,None,1])
        self.assertEqual(s.pathSum(tree1, 8), 3)
        tree2 = pathsum3.setupTree([1,-2,-3,1,3,-2,None,-1])
        self.assertEqual(s.pathSum(tree2, -1), 4)        
if __name__ == '__main__':
    unittest.main()
