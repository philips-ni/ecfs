
import unittest
import hammingWeight

class TestHammingweight(unittest.TestCase):
    def test_hammingWeight(self):
        s = hammingWeight.Solution()
        self.assertEqual(s.hammingWeight(11), 3)
        self.assertEqual(s.hammingWeight(128), 1)        
if __name__ == '__main__':
    unittest.main()
