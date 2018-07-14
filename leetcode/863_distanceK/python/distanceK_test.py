
import unittest
import distanceK

class TestDistancek(unittest.TestCase):
    def test_distanceK(self):
        s = distanceK.Solution()
        tree1 = distanceK.setupTree([3,5,1,6,2,0,8,None,None,7,4])
        print s.distanceK(tree1, 5, 2)
        
        self.assertEqual(s.distanceK(tree1, 5, 2), [7,4,1])
        self.assertEqual(s.distanceK(tree1, 5, 1), [6,2,3])
        self.assertEqual(s.distanceK(tree1, 5, 3), [0,8])
        tree2 = distanceK.setupTree([1])
        self.assertEqual(s.distanceK(tree2, 1, 3), [])

if __name__ == '__main__':
    unittest.main()
