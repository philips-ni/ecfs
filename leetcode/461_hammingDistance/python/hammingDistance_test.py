
import unittest
import hammingDistance

class TestHammingdistance(unittest.TestCase):
    def test_hammingDistance(self):
        s = hammingDistance.Solution()
        self.assertEqual(s.hammingDistance(1,4), 2)
        self.assertEqual(s.hammingDistance(0,4), 1)
if __name__ == '__main__':
    unittest.main()
