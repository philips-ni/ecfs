
import unittest
import missingNumber

class TestMissingnumber(unittest.TestCase):
    def test_missingNumber(self):
        s = missingNumber.Solution()
        self.assertEqual(s.missingNumber([3,0,1]), 2)
        self.assertEqual(s.missingNumber([9,6,4,2,3,5,7,0,1]), 8)
        
if __name__ == '__main__':
    unittest.main()
