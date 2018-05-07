
import unittest
import findKthLargest

class TestFindkthlargest(unittest.TestCase):
    def test_findKthLargest(self):
        s = findKthLargest.Solution()
        self.assertEqual(s.findKthLargest([3,2,1,5,6,4],2), 5)
        self.assertEqual(s.findKthLargest([3,2,3,1,2,4,5,5,6],4), 4)        
if __name__ == '__main__':
    unittest.main()
