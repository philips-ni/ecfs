
import unittest
import leastInterval

class TestLeastinterval(unittest.TestCase):
    def test_leastInterval(self):
        s = leastInterval.Solution()
        self.assertEqual(s.leastInterval(["A","A","A","B","B","B","C","C",],2), 8)
if __name__ == '__main__':
    unittest.main()
