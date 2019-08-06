
import unittest
import longestMountain

class TestLongestmountain(unittest.TestCase):
    def test_longestMountain(self):
        s = longestMountain.Solution()
        self.assertEqual(s.longestMountain([2,1,4,7,3,2,5,2]), 5 )
        self.assertEqual(s.longestMountain([2,2,2]), 0 )        
if __name__ == '__main__':
    unittest.main()
