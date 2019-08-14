
import unittest
import countPrimes

class TestCountprimes(unittest.TestCase):
    def test_countPrimes(self):
        s = countPrimes.Solution()
        self.assertEqual(s.countPrimes(10), 4)
        self.assertEqual(s.countPrimes(0), 0)
        self.assertEqual(s.countPrimes(1), 0)
        self.assertEqual(s.countPrimes(2), 0)
        self.assertEqual(s.countPrimes(3), 1)
        self.assertEqual(s.countPrimes(4), 2)                                        
if __name__ == '__main__':
    unittest.main()
