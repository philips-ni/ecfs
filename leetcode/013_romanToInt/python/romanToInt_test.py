import unittest
import romanToInt

class TestRomanToInt(unittest.TestCase):

    def test_romanToInt(self):
        s = romanToInt.Solution()
        self.assertEqual(-1,s.romanToInt("MIIIIVVVV"))
        self.assertEqual(1437,s.romanToInt("MCDXXXVII"))
        self.assertEqual(3000,s.romanToInt("MMM"))
        self.assertEqual(3333,s.romanToInt("MMMCCCXXXIII"))        
        self.assertEqual(199,s.romanToInt("CXCIX"))        
        self.assertEqual(190,s.romanToInt("CXC"))        

        self.assertEqual(1400,s.romanToInt("MCD"))        
        self.assertEqual(79,s.romanToInt("LXXIX"))        
        self.assertEqual(7,s.romanToInt("VII"))
        
        self.assertEqual(79,s.romanToInt("LXXIX"))

        self.assertEqual(100,s.romanToInt("C"))
        



    
if __name__ == '__main__':
    unittest.main()
    
