import unittest
import trappingRain

class TestTrappingrain(unittest.TestCase):
    def test_trap(self):
        s = trappingRain.Solution()
        self.assertEqual(s.trap([]), 0)                
        self.assertEqual(s.trap([1,0,1]), 1)        
        self.assertEqual(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(s.trap([0,1,2]), 0)
        self.assertEqual(s.trap([0]), 0)
        self.assertEqual(s.trap([1,2,1]), 0)
        self.assertEqual(s.trap([1,0,1,0,1]), 2)
                         

        
if __name__ == '__main__':
    unittest.main()
