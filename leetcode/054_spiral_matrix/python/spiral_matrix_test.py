
import unittest
import spiral_matrix

class TestSpiral_Matrix(unittest.TestCase):
    def test_spiralOrder(self):
        s = spiral_matrix.Solution()

        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12],
            [13,14,15,16]
        ]
        self.assertEqual(s.spiralOrder(m), [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])
        
        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]
        self.assertEqual(s.spiralOrder(m), [1,2,3,4,8,12,11,10,9,5,6,7])

        m = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        self.assertEqual(s.spiralOrder(m), [1,2,3,6,9,8,7,4,5])
        m = [
            []
        ]
        self.assertEqual(s.spiralOrder(m), [])

        m = [
            [1]
        ]
        self.assertEqual(s.spiralOrder(m), [1])
        
if __name__ == '__main__':
    unittest.main()
