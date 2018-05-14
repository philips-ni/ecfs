
import unittest
import rotate_image

class TestRotate_Image(unittest.TestCase):
    def test_rotate(self):
        s = rotate_image.Solution()
        m = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        r_m = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        s.rotate(m)
        # print m
        self.assertEqual(m,r_m)

        m = [
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ]
        r_m = [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
        ]
        s.rotate(m)
        self.assertEqual(m,r_m)
        
if __name__ == '__main__':
    unittest.main()
