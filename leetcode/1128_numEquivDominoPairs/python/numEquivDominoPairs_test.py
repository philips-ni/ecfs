
import unittest
import numEquivDominoPairs

class TestNumequivdominopairs(unittest.TestCase):
    def test_numEquivDominoPairs(self):
        s = numEquivDominoPairs.Solution()
        self.assertEqual(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]), 1)
if __name__ == '__main__':
    unittest.main()
