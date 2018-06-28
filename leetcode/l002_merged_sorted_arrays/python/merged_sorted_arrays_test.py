
import unittest
import merged_sorted_arrays

class TestMerged_Sorted_Arrays(unittest.TestCase):
    def test_merged_sorted_array(self):
        s = merged_sorted_arrays.Solution()
        self.assertEqual(s.merged_sorted_array([[1,3],[2,4,6],[5,7]]), [1,2,3,4,5,6,7])
        self.assertEqual(s.merged_sorted_array([[3,10],[2,4,6,100],[5,7]]), [2,3,4,5,6,7,10,100])        
if __name__ == '__main__':
    unittest.main()
