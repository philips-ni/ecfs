import unittest
import nqueens

class TestNqueens(unittest.TestCase):
    def test_solveNQueens(self):
        s = nqueens.Solution()
        expectedOut = [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],
            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ]
        self.assertEqual(s.solveNQueens(4), expectedOut)
        self.assertEqual(s.solveNQueens(0), [])
        self.assertEqual(s.solveNQueens(1), [['Q']])
        self.assertEqual(s.solveNQueens(2), [])
        self.assertEqual(s.solveNQueens(3), [])        
if __name__ == '__main__':
    unittest.main()
