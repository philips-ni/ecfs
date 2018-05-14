import unittest
import nqueens2

class TestNqueens(unittest.TestCase):
    def test_solveNQueens(self):
        s = nqueens2.Solution()
        self.assertEqual(s.totalNQueens(4), 2)
        self.assertEqual(s.totalNQueens(0), 0)
        self.assertEqual(s.totalNQueens(1), 1)
        self.assertEqual(s.totalNQueens(2), 0)
        self.assertEqual(s.totalNQueens(3), 0)        
if __name__ == '__main__':
    unittest.main()
