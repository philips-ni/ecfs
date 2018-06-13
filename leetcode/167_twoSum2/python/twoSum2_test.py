
import unittest
import twoSum2

class TestTwosum2(unittest.TestCase):
    def test_twoSum(self):
        s = twoSum2.Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [1,2])
        self.assertEqual(s.twoSum([2,7,11,15],18), [2,3])        
if __name__ == '__main__':
    unittest.main()
