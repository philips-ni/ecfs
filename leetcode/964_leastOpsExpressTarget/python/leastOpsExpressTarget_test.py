import unittest
import leastOpsExpressTarget

class TestLeastopsexpresstarget(unittest.TestCase):
    def test_leastOpsExpressTarget(self):
        s = leastOpsExpressTarget.Solution()
        self.assertEqual(s.leastOpsExpressTarget(3, 18), 3)        
        self.assertEqual(s.leastOpsExpressTarget(3, 19), 5)
        self.assertEqual(s.leastOpsExpressTarget(5, 501), 8)
        self.assertEqual(s.leastOpsExpressTarget(100, 100000000), 3)
if __name__ == '__main__':
    unittest.main()
