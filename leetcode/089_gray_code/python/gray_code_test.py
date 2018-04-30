
import unittest
import gray_code

class TestGray_Code(unittest.TestCase):
    def test_grayCode(self):
        s = gray_code.Solution()
        self.assertEqual(s.grayCode(0), [])        
        self.assertEqual(s.grayCode(1), [0,1])
        self.assertEqual(s.grayCode(2), [0,1,3,2])
        self.assertEqual(s.grayCode(3), [0,1,3,2,6,7,5,4])                
        
if __name__ == '__main__':
    unittest.main()
