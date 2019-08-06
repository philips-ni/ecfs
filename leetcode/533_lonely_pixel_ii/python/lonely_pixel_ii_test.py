
import unittest
import lonely_pixel_ii

class TestLonely_Pixel_Ii(unittest.TestCase):
    def test_findBlackPixel(self):
        s = lonely_pixel_ii.Solution()
        picture = [['W', 'B', 'W', 'B', 'B', 'W'],    
                   ['W', 'B', 'W', 'B', 'B', 'W'],    
                   ['W', 'B', 'W', 'B', 'B', 'W'],    
                   ['W', 'W', 'B', 'W', 'B', 'W']] 
        self.assertEqual(s.findBlackPixel(picture, 3), 6)
        self.assertEqual(s.findBlackPixel(picture, 2), 0)
        
if __name__ == '__main__':
    unittest.main()
