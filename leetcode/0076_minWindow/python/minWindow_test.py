
import unittest
import minWindow

class TestMinwindow(unittest.TestCase):
    def test_minWindow(self):
        s = minWindow.Solution()
        self.assertEqual(s.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(s.minWindow("ADOBECODEBANC", "ABCC"), "CODEBANC")        
if __name__ == '__main__':
    unittest.main()
