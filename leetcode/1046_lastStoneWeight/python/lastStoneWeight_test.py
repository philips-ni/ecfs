
import unittest
import lastStoneWeight

class TestLaststoneweight(unittest.TestCase):
    def test_lastStoneWeight(self):
        s = lastStoneWeight.Solution()
        self.assertEqual(s.lastStoneWeight([2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight([1,1]), 0)
        self.assertEqual(s.lastStoneWeight([3, 1,1]), 1)                
if __name__ == '__main__':
    unittest.main()
