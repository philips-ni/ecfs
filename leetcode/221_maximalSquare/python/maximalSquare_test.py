
import unittest
import maximalSquare

class TestMaximalsquare(unittest.TestCase):
    def test_maximalSquare(self):
        s = maximalSquare.Solution()
        matrix =[
            [1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0]]
        self.assertEqual(s.maximalSquare(matrix), 4)
if __name__ == '__main__':
    unittest.main()
