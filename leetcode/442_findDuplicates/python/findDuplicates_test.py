
import unittest
import findDuplicates

class TestFindduplicates(unittest.TestCase):
    def test_findDuplicates(self):
        s = findDuplicates.Solution()
        self.assertEqual(s.findDuplicates([4,3,2,7,8,2,3,1]),[2,3] )
        # self.assertEqual(s.findDuplicates([2,2]),[2] )        
if __name__ == '__main__':
    unittest.main()
