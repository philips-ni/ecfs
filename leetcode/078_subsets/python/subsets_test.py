
import unittest
import subsets

class TestSubsets(unittest.TestCase):
    def test_subsets(self):
        s = subsets.Solution()
        sets = s.subsets([1,2,3])
        print sets
        sets = s.subsets([1,2])
        print sets
        sets = s.subsets([1])
        print sets

if __name__ == '__main__':
    unittest.main()
