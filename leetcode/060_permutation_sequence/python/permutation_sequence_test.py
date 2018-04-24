
import unittest
import permutation_sequence

class TestPermutation_Sequence(unittest.TestCase):
    def test_getPermutation(self):
        s = permutation_sequence.Solution()
        self.assertEqual(s.getPermutation(2, 2), "21")        
        self.assertEqual(s.getPermutation(3, 3), "213")
        self.assertEqual(s.getPermutation(4, 9), "2314")
        self.assertEqual(s.getPermutation(1, 1), "1")

        
if __name__ == '__main__':
    unittest.main()
