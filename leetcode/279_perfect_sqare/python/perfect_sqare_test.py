
import unittest
import perfect_sqare

class TestPerfect_Sqare(unittest.TestCase):
    def test_numSquares(self):
        s = perfect_sqare.Solution()
        self.assertEqual(s.numSquares(12), 3)
        self.assertEqual(s.numSquares(13), 2)        
if __name__ == '__main__':
    unittest.main()
