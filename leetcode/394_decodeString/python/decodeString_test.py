
import unittest
import decodeString

class TestDecodestring(unittest.TestCase):
    def test_decodeString(self):
        s = decodeString.Solution()
        self.assertEqual(s.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(s.decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(s.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
if __name__ == '__main__':
    unittest.main()
