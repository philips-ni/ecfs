
import unittest
import reconstruct_original_digits

class TestReconstruct_Original_Digits(unittest.TestCase):
    def test_originalDigits(self):
        s = reconstruct_original_digits.Solution()
        self.assertEqual(s.originalDigits("owoztneoer"), "012")
        self.assertEqual(s.originalDigits("fviefuro"), "45")        
if __name__ == '__main__':
    unittest.main()
