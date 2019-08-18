
import unittest
import split_array_into_consecutive_subsequences

class TestSplit_Array_Into_Consecutive_Subsequences(unittest.TestCase):
    def test_isPossible(self):
        s = split_array_into_consecutive_subsequences.Solution()
        # self.assertEqual(s.isPossible([1,2,3,4,4,5]), False)
        self.assertEqual(s.isPossible([1,2,3,3,4,4,5,5]), True)
        # self.assertEqual(s.isPossible([1,2,3,3,4,5]), True)                
if __name__ == '__main__':
    unittest.main()
