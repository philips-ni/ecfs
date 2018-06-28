
import unittest
import Sum_of_Two_Integers

class TestSum_Of_Two_Integers(unittest.TestCase):
    def test_getSum(self):
        s = Sum_of_Two_Integers.Solution()
        self.assertEqual(s.getSum(1,2), 3)
        self.assertEqual(s.getSum(0,29), 29)        
        self.assertEqual(s.getSum(18,29), 47)
        self.assertEqual(s.getSum(1,2), 3)                
if __name__ == '__main__':
    unittest.main()
