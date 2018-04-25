
import unittest
import merge_intervals

class TestMerge_Intervals(unittest.TestCase):
    def test_merge(self):
        s = merge_intervals.Solution()
        self.assertEqual(s.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(s.merge([[1,4],[4,5]]), [[1,5]])
        
if __name__ == '__main__':
    unittest.main()
