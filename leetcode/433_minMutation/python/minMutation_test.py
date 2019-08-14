
import unittest
import minMutation

class TestMinmutation(unittest.TestCase):
    def test_minMutation(self):
        s = minMutation.Solution()
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        self.assertEqual(s.minMutation(start, end, bank), 1)
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        self.assertEqual(s.minMutation(start, end, bank), 2)
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        self.assertEqual(s.minMutation(start, end, bank), 3)        
        
if __name__ == '__main__':
    unittest.main()
