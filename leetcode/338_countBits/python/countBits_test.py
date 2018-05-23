
import unittest
import countBits

class TestCountbits(unittest.TestCase):
    def test_countBits(self):
        s = countBits.Solution()
        self.assertEqual(s.countBits(5), [0,1,1,2,1,2])
        self.assertEqual(s.countBits(1), [0,1])
if __name__ == '__main__':
    unittest.main()
