import unittest
import NumbersAtMostNGivenDigitSet

class TestNumbersatmostngivendigitset(unittest.TestCase):
    def test_atMostNGivenDigitSet(self):
        s = NumbersAtMostNGivenDigitSet.Solution()
        D = ["1","3","5","7"]
        N = 100
        self.assertEqual(s.atMostNGivenDigitSet(D,N), 20)

        D = ["1","3","5"]
        N = 32
        self.assertEqual(s.atMostNGivenDigitSet(D,N), 7)

        D = ["1","4","9"]
        N = 1000000000
        self.assertEqual(s.atMostNGivenDigitSet(D,N), 29523)

        D = ["3","4","8"]
        N = 4
        self.assertEqual(s.atMostNGivenDigitSet(D,N), 2)

        D = ["1","5","7","8"]
        N = 10212
        self.assertEqual(s.atMostNGivenDigitSet(D,N), 340)

        
#         D = ["1","4","9"]
#         N = 1000000000
#         self.assertEqual(s.atMostNGivenDigitSet(D,N), 29523)
#

if __name__ == '__main__':
    unittest.main()
