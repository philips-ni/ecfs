
import unittest
import length_of_last_word

class TestLength_Of_Last_Word(unittest.TestCase):
    def test_lengthOfLastWord(self):
        s = length_of_last_word.Solution()
        self.assertEqual(s.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(s.lengthOfLastWord(""), 0)
        self.assertEqual(s.lengthOfLastWord("   "), 0)
        self.assertEqual(s.lengthOfLastWord("abc   "), 3)
        
if __name__ == '__main__':
    unittest.main()
