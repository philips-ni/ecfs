
import unittest
import searchInRotatedSortedArray

class TestSearchinrotatedsortedarray(unittest.TestCase):
    def test_search(self):
        s = searchInRotatedSortedArray.Solution()
        self.assertEqual(s.search([4, 5, 6, 7,  0,  1,  2], 0), 4 )        
        self.assertEqual(s.search([5,1,3], 3), 2)
        self.assertEqual(s.search([], 5), -1 )        
        self.assertEqual(s.search([4, 5, 6, 7,  0,  1,  2], 1), 5 )        
        self.assertEqual(s.search([4, 5, 6, 7,  0,  1,  2], 5), 1 )
        self.assertEqual(s.search([4, 5, 6, 7,  0,  1,  2], 100), -1 )                
        
if __name__ == '__main__':
    unittest.main()
