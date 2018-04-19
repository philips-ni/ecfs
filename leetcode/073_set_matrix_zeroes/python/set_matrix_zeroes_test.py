
import unittest
import set_matrix_zeroes

class TestSet_Matrix_Zeroes(unittest.TestCase):
    def test_setZeroes(self):
        s = set_matrix_zeroes.Solution()
        l1 = [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ]
        expected_l1_out = [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
        s.setZeroes(l1)
        self.assertEqual(l1, expected_l1_out)

        l2 = [
            [0,1]
        ]
        expected_l2_out = [
            [0,0]
        ]
        s.setZeroes(l2)        
        self.assertEqual(l2, expected_l2_out)

        l3 = [
            []
        ]
        expected_l3_out = [
            []
        ]
        s.setZeroes(l3)                
        self.assertEqual(l3, expected_l3_out)

        l4 = [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ]
        expected_l4_out = [
            [0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]
        ]
        s.setZeroes(l4)                        
        self.assertEqual(l4, expected_l4_out)
        
        
if __name__ == '__main__':
    unittest.main()
