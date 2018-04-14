import unittest
import intToRoman

class TestIntToRoman(unittest.TestCase):

    def test_intToRoman(self):
        s = intToRoman.Solution()
        self.assertEqual("VII",s.intToRoman(7))
        self.assertEqual("LXXIX",s.intToRoman(79))
        self.assertEqual("CXCIX",s.intToRoman(199))
        self.assertEqual("C",s.intToRoman(100))
        self.assertEqual("MMMCCCXXXIII",s.intToRoman(3333))
        self.assertEqual("MCD",s.intToRoman(1400))

if __name__ == '__main__':
    unittest.main()
        
