import unittest
import palnum
class TestPalNum(unittest.TestCase):

    def test_isPalindrome(self):
        s = palnum.Solution()
        self.assertEqual(True,s.isPalindrome(202))
        self.assertEqual(True,s.isPalindrome(2002))
        self.assertEqual(False,s.isPalindrome(2102))
        self.assertEqual(True,s.isPalindrome(22))
        self.assertEqual(False,s.isPalindrome(21))
        self.assertEqual(False,s.isPalindrome(-22))
        self.assertEqual(True,s.isPalindrome(20022002))
    def test_getNumLen(self):
        s = palnum.Solution()
        self.assertEqual(3,s.getNumLen(123))

if __name__ == '__main__':
    unittest.main()
        
