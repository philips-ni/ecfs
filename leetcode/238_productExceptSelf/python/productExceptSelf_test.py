
import unittest
import productExceptSelf

class TestProductexceptself(unittest.TestCase):
    def test_productExceptSelf(self):
        s = productExceptSelf.Solution()
        self.assertEqual(s.productExceptSelf([1,2,3,4]), [24,12,8,6])
if __name__ == '__main__':
    unittest.main()
