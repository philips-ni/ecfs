
import unittest
import Permutations

class TestPermutations(unittest.TestCase):
    def test_permute(self):
        s = Permutations.Solution()
        self.assertEqual(s.permute([]), [[]])
        # self.assertEqual(s.permute([1]), [[1]])
        self.assertEqual(s.permute([1,2]), [[1,2],[2,1]])
        self.assertEqual(s.permute([1,2,3]), [[1,2,3],[3,1,2],[2,1,3],[3,2,1],[1,3,2],[2,3,1]])

if __name__ == '__main__':
    unittest.main()
