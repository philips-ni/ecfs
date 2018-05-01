import unittest
import zigzag

class TestZigZag(unittest.TestCase):

    def test_convert2(self):
        s = zigzag.Solution()
        s1 = "PAYPALISHIRING"
        s2 = ""
        s3 = "abc"
        self.assertEqual("acb",s.convert2("abc", 2))
        self.assertEqual("acdb",s.convert2("abcd", 2))
        self.assertEqual("PAHNAPLSIIGYIR",s.convert2(s1, 3))
        self.assertEqual("PINAASRGYLHIPI",s.convert2(s1, 4))
        self.assertEqual("PHALIGYIRPSIAN",s.convert2(s1, 5))
        self.assertEqual("",s.convert2(s2, 1))
        self.assertEqual("",s.convert2(s2, 2))
        self.assertEqual("abc",s.convert2(s3, 3))
        self.assertEqual("abc",s.convert2(s3, 4))
        self.assertEqual("a",s.convert2("a", 1))
        self.assertEqual("ab",s.convert2("ab", 2))


    def test_convert(self):
        s = zigzag.Solution()
        s1 = "PAYPALISHIRING"
        self.assertEqual("acb",s.convert("abc", 2))
        self.assertEqual("PAHNAPLSIIGYIR",s.convert(s1, 3))
        self.assertEqual("AEBDFC",s.convert2("ABCDEF", 3))
        


if __name__ == '__main__':
    unittest.main()
        
