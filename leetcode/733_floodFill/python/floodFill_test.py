
import unittest
import floodFill

class TestFloodfill(unittest.TestCase):
    def test_floodFill(self):
        s = floodFill.Solution()
        image = [[1,1,1],[1,1,0],[1,0,1]]
        self.assertEqual(s.floodFill(image, 1,1,2), [[2,2,2],[2,2,0],[2,0,1]])
        
if __name__ == '__main__':
    unittest.main()
