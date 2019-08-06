
import unittest
import delete_columns_to_make_sorted_ii

class TestDelete_Columns_To_Make_Sorted_Ii(unittest.TestCase):
    def test_minDeletionSize(self):
        s = delete_columns_to_make_sorted_ii.Solution()
        self.assertEqual(s.minDeletionSize(["xga","xfb","xfa"]), 2)
        self.assertEqual(s.minDeletionSize(["xga","xfb","yfa"]), 1)
"""                
        self.assertEqual(s.minDeletionSize(["xfa","yfb","yfa"]), 1)        
        self.assertEqual(s.minDeletionSize(["ca","bb","ac"]), 1)
        self.assertEqual(s.minDeletionSize(["xc","yb","za"]), 0)
        self.assertEqual(s.minDeletionSize(["zyx","wvu","tsr"]), 3)
        self.assertEqual(s.minDeletionSize(["a","b","c"]), 0)
        self.assertEqual(s.minDeletionSize(["a","a","c"]), 0)
        self.assertEqual(s.minDeletionSize(["a","c","a"]), 1)                
        self.assertEqual(s.minDeletionSize(["","",""]), 0)        
"""
if __name__ == '__main__':
    unittest.main()
