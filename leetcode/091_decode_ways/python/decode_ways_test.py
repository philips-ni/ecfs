
import unittest
import decode_ways

class TestDecode_Ways(unittest.TestCase):
    def test_numDecodings(self):
        s = decode_ways.Solution()
        self.assertEqual(s.numDecodings("01"), 0)
        self.assertEqual(s.numDecodings("0"), 0)                
        self.assertEqual(s.numDecodings("12"), 2)
        self.assertEqual(s.numDecodings("236"), 2)
        self.assertEqual(s.numDecodings("237"), 2)
        self.assertEqual(s.numDecodings("2372"), 2)                
        self.assertEqual(s.numDecodings("1266"), 3)        
if __name__ == '__main__':
    unittest.main()
