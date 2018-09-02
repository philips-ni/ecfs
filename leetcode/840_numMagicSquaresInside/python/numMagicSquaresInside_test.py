
import unittest
import numMagicSquaresInside

class TestNummagicsquaresinside(unittest.TestCase):
    def test_numMagicSquaresInside(self):
        s = numMagicSquaresInside.Solution()
        d = [[4,3,8,4],
             [9,5,1,9],
             [2,7,6,2]]
        self.assertEqual(s.numMagicSquaresInside(d), 1)
        d = [[1,2,3]]
        self.assertEqual(s.numMagicSquaresInside(d), 0)
        d = [[1,2,3],
             [1,2,3],
             [1,2,4]             
             ]        
        self.assertEqual(s.numMagicSquaresInside(d), 0)

        d = [[10,3,5],
             [1,6,11],
             [7,9,2]             
             ]        
        self.assertEqual(s.numMagicSquaresInside(d), 0)
        d = [[3,7,4,3],[2,8,7,4],[7,2,1,5],[4,6,9,3]]
        self.assertEqual(s.numMagicSquaresInside(d), 0)
        d = [[5,4,7,8,5,4,6,8,2,9],[5,3,6,8,1,5,1,1,8,5],[8,9,6,8,4,7,3,4,9,1],[9,3,8,9,2,8,3,8,7,1],[1,1,1,7,3,3,9,1,8,7],[1,5,5,7,1,6,7,9,3,4],[2,3,3,8,8,1,1,6,5,7],[7,8,5,4,7,9,4,6,5,3],[8,5,2,7,1,3,7,2,8,9],[4,9,4,3,9,4,5,4,7,1]]
        self.assertEqual(s.numMagicSquaresInside(d), 0)
        d = [[1,8,6],[10,5,0],[4,2,9]]
        self.assertEqual(s.numMagicSquaresInside(d), 0)        
        
if __name__ == '__main__':
    unittest.main()
