
import unittest
import combinations

class TestCombinations(unittest.TestCase):
    def test_combine(self):
        s = combinations.Solution()
        out = s.combine(4,2)
        print out
if __name__ == '__main__':
    unittest.main()
