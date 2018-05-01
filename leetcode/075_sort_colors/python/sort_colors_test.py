
import unittest
import sort_colors

class TestSort_Colors(unittest.TestCase):
    def test_sortColors(self):
        s = sort_colors.Solution()

        l = [1,2,0]
        s.sortColors(l)        
        self.assertEqual(l, [0,1,2])
        
        l = [2,0,2,1,1,0]
        s.sortColors(l)
        self.assertEqual(l, [0,0,1,1,2,2])

        l = [1]
        s.sortColors(l)
        self.assertEqual(l, [1])

        l = [1,1,1,1]
        s.sortColors(l)
        self.assertEqual(l, [1,1,1,1])

        l = [2,1,1,1,1]
        s.sortColors(l)
        self.assertEqual(l, [1,1,1,1,2])

        l = []
        s.sortColors(l)
        self.assertEqual(l, [])

        
if __name__ == '__main__':
    unittest.main()
