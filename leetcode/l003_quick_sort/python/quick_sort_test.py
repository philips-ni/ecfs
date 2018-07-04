
import unittest
import quick_sort

class TestQuick_Sort(unittest.TestCase):
    def test_quick_sort(self):
        s = quick_sort.Solution()
        l = [1,3,2,4]
        s.quick_sort(l)
        self.assertEqual(l,[1,2,3,4])
        l = [1]
        s.quick_sort(l)
        self.assertEqual(l,[1])
        
if __name__ == '__main__':
    unittest.main()
