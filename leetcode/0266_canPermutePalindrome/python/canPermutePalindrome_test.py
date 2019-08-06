
import unittest
import canPermutePalindrome

class TestCanpermutepalindrome(unittest.TestCase):
    def test_canPermutePalindrome(self):
        s = canPermutePalindrome.Solution()
        self.assertEqual(s.canPermutePalindrome("code"), False)
        self.assertEqual(s.canPermutePalindrome("aab"), True)
        self.assertEqual(s.canPermutePalindrome("carerac"), True)        
if __name__ == '__main__':
    unittest.main()
