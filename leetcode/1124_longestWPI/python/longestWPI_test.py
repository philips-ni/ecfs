
import unittest
import longestWPI

class TestLongestwpi(unittest.TestCase):
    def test_longestWPI(self):
        s = longestWPI.Solution()
        self.assertEqual(s.longestWPI([9,9,6,0,6,6,9]), 3)
        # self.assertEqual(s.longestWPI([9,9,6,6,9,6,9]), 7)        
if __name__ == '__main__':
    unittest.main()
