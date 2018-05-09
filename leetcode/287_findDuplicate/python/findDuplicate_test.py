
import unittest
import findDuplicate

class TestFindduplicate(unittest.TestCase):
    def test_findDuplicate(self):
        s = findDuplicate.Solution()
        # self.assertEqual(s.findDuplicate([1,2,2,3]),2 )
        self.assertEqual(s.findDuplicate([1,4,3,2,3]),3 )        
if __name__ == '__main__':
    unittest.main()
