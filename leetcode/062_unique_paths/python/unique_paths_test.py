
import unittest
import unique_paths

class TestUnique_Paths(unittest.TestCase):
    def test_uniquePaths(self):
        s = unique_paths.Solution()
        self.assertEqual(s.uniquePaths(3,2), 3)
        self.assertEqual(s.uniquePaths(7,3), 28)
        # self.assertEqual(s.uniquePaths(20,20), 280)                
if __name__ == '__main__':
    unittest.main()
