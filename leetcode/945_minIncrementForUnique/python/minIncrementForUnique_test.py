
import unittest
import minIncrementForUnique

class TestMinincrementforunique(unittest.TestCase):
    def test_minIncrementForUnique(self):
        s = minIncrementForUnique.Solution()
        self.assertEqual(s.minIncrementForUnique([1,2,2]), 1)
        self.assertEqual(s.minIncrementForUnique([3,2,1,2,1,7]), 6)        
if __name__ == '__main__':
    unittest.main()
