
import unittest
import bit_add

class TestBit_Add(unittest.TestCase):
    def test_bit_add(self):
        s = bit_add.Solution()
        self.assertEqual(s.bit_add(72,9),81 )        
        self.assertEqual(s.bit_add(5,6),11 )
        self.assertEqual(s.bit_add(5,-6),-1 )

        # self.assertEqual(s.bit_add(10,-1),9 )                
        self.assertEqual(s.bit_add(0,10),10 )
        self.assertEqual(s.bit_add(100,10),110 )

    def test_bit_minus(self):
        s = bit_add.Solution()
        self.assertEqual(s.bit_minus(5,6),-1 )
        # self.assertEqual(s.bit_minus(100,10),90 )
        # self.assertEqual(s.bit_minus(0,10),-10 )
        # self.assertEqual(s.bit_minus(10,1),9 ) #  =====> dead loop


    def test_bit_mul(self):
        s = bit_add.Solution()
        self.assertEqual(s.bit_mul(5,6),30 )
        self.assertEqual(s.bit_mul(9,9),81 )        
        
if __name__ == '__main__':
    unittest.main()
