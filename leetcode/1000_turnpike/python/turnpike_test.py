
import unittest
import turnpike

class TestTurnpike(unittest.TestCase):
    def test_turnpike(self):
        s = turnpike.Solution()
        self.assertEqual(s.turnpike(), )
if __name__ == '__main__':
    unittest.main()
