
import unittest
import find_pivot_index

class TestFind_Pivot_Index(unittest.TestCase):
    def test_pivotIndex(self):
        s = find_pivot_index.Solution()
        self.assertEqual(s.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(s.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(s.pivotIndex([1, 2, 2,3,2,2,1]), 3)
        self.assertEqual(s.pivotIndex([-1,-1,-1,0,1,1]), 0)
        self.assertEqual(s.pivotIndex([-1,-1,0,1,1,1]), 5)        

if __name__ == '__main__':
    unittest.main()
