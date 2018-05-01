
import unittest
import plus_one

class TestPlus_One(unittest.TestCase):
    def test_plusOne(self):
        s = plus_one.Solution()
        self.assertEqual(s.plusOne([9]), [1,0])
        self.assertEqual(s.plusOne([1,0]), [1,1])
        
if __name__ == '__main__':
    unittest.main()
