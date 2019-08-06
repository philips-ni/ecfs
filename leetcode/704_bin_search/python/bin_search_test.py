
import unittest
import bin_search

class TestBin_Search(unittest.TestCase):
    def test_search(self):
        s = bin_search.Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([1], 2), -1)
        self.assertEqual(s.search([-1,0,3,5,9,12], 2), -1)
        self.assertEqual(s.search([], 1), -1)

        self.assertEqual(s.search([1,2], 1), 0)                        
if __name__ == '__main__':
    unittest.main()
