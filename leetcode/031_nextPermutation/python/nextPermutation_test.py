
import unittest
import nextPermutation

class TestNextpermutation(unittest.TestCase):
    def test_nextPermutation(self):
        s = nextPermutation.Solution()
        l = [5,1,1]
        s.nextPermutation(l)
        self.assertEqual(l,[1,1,5])

        l = [1,2]
        s.nextPermutation(l)
        self.assertEqual(l,[2,1])

        l = [3,2,1]
        s.nextPermutation(l)
        self.assertEqual(l,[1,2,3])

        l = [1,5,8,4,7,6,5,3,1]
        s.nextPermutation(l)
        self.assertEqual(l,[1,5,8,5,1,3,4,6,7])
        

        
#        
#        self.assertEqual(s.nextPermutation([5,1,1]), [1,1,5])        
#        self.assertEqual(s.nextPermutation([1,2]), [2,1])
#        self.assertEqual(s.nextPermutation([1]), [1])
#        self.assertEqual(s.nextPermutation([]), [])                
#        self.assertEqual(s.nextPermutation([3,2,1]), [1,2,3])                
#        self.assertEqual(s.nextPermutation([1,2,3]), [1,3,2])
#        self.assertEqual(s.nextPermutation([1,1,5]), [1,5,1])
#        self.assertEqual(s.nextPermutation([1,5,8,4,7,6,5,3,1]), [1,5,8,5,1,3,4,6,7])        
        
if __name__ == '__main__':
    unittest.main()
