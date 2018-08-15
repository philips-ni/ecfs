import unittest
import range_sum_query

class TestRange_Sum_Query(unittest.TestCase):
    def test_sumRange(self):
        nums = [1,3,5]
        obj = range_sum_query.NumArray(nums)
        obj.update(1,2)
        self.assertEqual(obj.sumRange(0,2), 8)
        
if __name__ == '__main__':
    unittest.main()
