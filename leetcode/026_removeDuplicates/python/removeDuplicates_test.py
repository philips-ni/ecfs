
import unittest
import removeDuplicates

class TestRemoveduplicates(unittest.TestCase):
    def test_removeDuplicates(self):
        s = removeDuplicates.Solution()

        
        l1 = [1,1,2]
        ret = s.removeDuplicates(l1)
        self.assertEqual(ret, 2 )
        self.assertEqual(l1[0], 1)
        self.assertEqual(l1[1], 2)
        print l1
        
        l2 = [1,2]
        self.assertEqual(s.removeDuplicates(l2), 2 )
        self.assertEqual(l2[0], 1)
        self.assertEqual(l2[1], 2)
        
        l3 = []
        self.assertEqual(s.removeDuplicates(l3), 0 )
        l4 = [1,1,2,2,3,3,3]
        self.assertEqual(s.removeDuplicates(l4), 3 )
        self.assertEqual(l4[0], 1)
        self.assertEqual(l4[1], 2)
        self.assertEqual(l4[2], 3)        

        print l4
        
if __name__ == '__main__':
    unittest.main()
