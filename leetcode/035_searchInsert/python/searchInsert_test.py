
import unittest
import searchInsert

class TestSearchinsert(unittest.TestCase):
    def test_searchInsert(self):
        s = searchInsert.Solution()
        self.assertEqual(s.searchInsert([1,3,5,6], 2),1 )                        
        self.assertEqual(s.searchInsert([1,3,5,6], 5),2 )
        self.assertEqual(s.searchInsert([1,3,5,6], 7),4 )
        self.assertEqual(s.searchInsert([1,3,5,6], 0),0 )        
if __name__ == '__main__':
    unittest.main()
