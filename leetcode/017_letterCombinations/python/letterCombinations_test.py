
import unittest
import letterCombinations

class TestLettercombinations(unittest.TestCase):
    def test_letterCombinations(self):
        s = letterCombinations.Solution()
        self.assertEqual(s.letterCombinations("23"), \
                         ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(s.letterCombinations("2"), \
                         ["a","b","c"])
        self.assertEqual(s.letterCombinations(""), \
                         [])
        
        
        
if __name__ == '__main__':
    unittest.main()
