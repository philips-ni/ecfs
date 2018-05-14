import unittest
import single_number

class TestSingle_Number(unittest.TestCase):
    def test_singleNumber(self):
        s = single_number.Solution()
        self.assertEqual(s.singleNumber([2,2,1]), 1)
        self.assertEqual(s.singleNumber([4,1,2,1,2]), 4)        
        
if __name__ == '__main__':
    unittest.main()
