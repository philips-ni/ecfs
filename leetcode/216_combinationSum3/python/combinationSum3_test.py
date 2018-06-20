
import unittest
import combinationSum3

class TestCombinationsum3(unittest.TestCase):
    def test_combinationSum3(self):
        s = combinationSum3.Solution()
        self.assertEqual(s.combinationSum3(3,7), [[1,2,4]])
        self.assertEqual(s.combinationSum3(3,9), [[1,2,6],[1,3,5],[2,3,4]])        
if __name__ == '__main__':
    unittest.main()
