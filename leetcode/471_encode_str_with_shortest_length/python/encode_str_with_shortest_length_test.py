import unittest
import encode_str_with_shortest_length

class TestEncode_Str_With_Shortest_Length(unittest.TestCase):
    def test_encode(self):
        s = encode_str_with_shortest_length.Solution()
        self.assertEqual(s.encode("aaa"), "aaa")
        self.assertEqual(s.encode("aaaaa"), "5[a]")
        self.assertEqual(s.encode("aabcaabcd"), "2[aabc]d")
        
if __name__ == '__main__':
    unittest.main()
