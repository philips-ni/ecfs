
import unittest
import escapeGhosts

class TestEscapeghosts(unittest.TestCase):
    def test_escapeGhosts(self):
        s = escapeGhosts.Solution()
        self.assertEqual(s.escapeGhosts([[1, 0], [0, 3]], [0,1]), True)
        self.assertEqual(s.escapeGhosts([[2, 0]], [1,0]), False)
        self.assertEqual(s.escapeGhosts([[1, 0]], [2,0]), False)                
if __name__ == '__main__':
    unittest.main()
