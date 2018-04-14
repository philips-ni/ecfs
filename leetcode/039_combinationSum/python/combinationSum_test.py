
import unittest
import combinationSum

class TestCombinationsum(unittest.TestCase):
    def test_combinationSum(self):
        s = combinationSum.Solution()
        expectedRet = [
            [2, 2, 3],
            [7]      
        ]
        self.assertEqual(s.combinationSum([2, 3, 6, 7], 7), expectedRet)
if __name__ == '__main__':
    unittest.main()
