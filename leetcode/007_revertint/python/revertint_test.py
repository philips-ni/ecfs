import unittest
import revertint

class TestRevertInt(unittest.TestCase):

    def test_reverse(self):
        s = revertint.Solution()
        self.assertEqual(321,s.reverse(123))
        self.assertEqual(-321,s.reverse(-1230))
        self.assertEqual(21,s.reverse(120))
        self.assertEqual(0,s.reverse(1200000000000009))
        


if __name__ == '__main__':
    unittest.main()
        
