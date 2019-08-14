
import unittest
import wiggle_sort_ii

class TestWiggle_Sort_Ii(unittest.TestCase):
    def test_wiggleSort(self):
        s = wiggle_sort_ii.Solution()
        nums = [1, 5, 1, 1, 6, 4]
        s.wiggleSort(nums)
        print(nums)
        
if __name__ == '__main__':
    unittest.main()
