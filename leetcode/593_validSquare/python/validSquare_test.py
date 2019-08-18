
import unittest
import validSquare

class TestValidsquare(unittest.TestCase):
    def test_validSquare(self):
        s = validSquare.Solution()
        p1 = [0,0]
        p2 = [1,1]
        p3 = [1,0]
        p4 = [0,1]
        self.assertEqual(s.validSquare(p1,p2,p3,p4), True)
if __name__ == '__main__':
    unittest.main()
