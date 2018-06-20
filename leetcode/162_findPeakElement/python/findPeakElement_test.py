
import unittest
import findPeakElement

class TestFindpeakelement(unittest.TestCase):
    def test_findPeakElement(self):
        s = findPeakElement.Solution()
        self.assertEqual(s.findPeakElement([1,2,3,1]), [2])
        self.assertEqual(s.findPeakElement([1,2,1,3,5,6,4]), [1,5])        
if __name__ == '__main__':
    unittest.main()
