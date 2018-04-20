
import unittest
import remove_duplicates2

class TestRemove_Duplicates2(unittest.TestCase):
    def test_removeDuplicates(self):
        s = remove_duplicates2.Solution()

        l =  [1,1,1,2,2,2,3,3,3]
        # s.removeDuplicates(l)
        # print l
        self.assertEqual(s.removeDuplicates(l), 6)
        print l
        l =  [1,1,1,1]
        self.assertEqual(s.removeDuplicates(l), 2)
        print l
       
        l =  [3,1,1,1,1]
        self.assertEqual(s.removeDuplicates(l), 3)
        print l
        
        l = [1,1,1,1,1,2,2,3]
        self.assertEqual(s.removeDuplicates(l), 5)
        print l
        
        l =  [0,0,1,1,1,1,2,3,3]
        self.assertEqual(s.removeDuplicates(l), 7)
        print l

        l =  [1,1]
        self.assertEqual(s.removeDuplicates(l), 2)
        print l
#

        
        
if __name__ == '__main__':
    unittest.main()
