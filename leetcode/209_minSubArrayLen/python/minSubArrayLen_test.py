
import unittest
import minSubArrayLen

class TestMinsubarraylen(unittest.TestCase):
    def test_minSubArrayLen(self):
        s = minSubArrayLen.Solution()
        self.assertEqual(s.minSubArrayLen(7,[2,3,1,2,4,3]), 2)
        self.assertEqual(s.minSubArrayLen(9,[2,3,2,2,4,3]), 3)
        self.assertEqual(s.minSubArrayLen(90,[2,3,2,2,4,3]), 0)
        self.assertEqual(s.minSubArrayLen(11,[2,3,2,2,4,3]), 4)                        
if __name__ == '__main__':
    unittest.main()
