
import unittest
import multiplyStr

class TestMultiplystr(unittest.TestCase):
    def test_multiply(self):
        s = multiplyStr.Solution()
        # self.assertEqual(s.multiply("2","3"), "6")
        # self.assertEqual(s.multiply("20","3"), "60")
        self.assertEqual(s.multiply("123","456"), "56088")        
if __name__ == '__main__':
    unittest.main()
