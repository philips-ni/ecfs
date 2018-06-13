
import unittest
import max_product_subarray

class TestMax_Product_Subarray(unittest.TestCase):
        
    def test_maxProduct(self):
        s = max_product_subarray.Solution()
        self.assertEqual(s.maxProduct([2,3,-2,4]), 6)
        self.assertEqual(s.maxProduct([-2,0,-1]), 0)
        self.assertEqual(s.maxProduct([-2,-2,8,-1,1000]), 16000)
        self.assertEqual(s.maxProduct([-2]),-2)
if __name__ == '__main__':
    unittest.main()
