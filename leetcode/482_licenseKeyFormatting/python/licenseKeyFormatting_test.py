
import unittest
import licenseKeyFormatting

class TestLicensekeyformatting(unittest.TestCase):
    def test_licenseKeyFormatting(self):
        s = licenseKeyFormatting.Solution()
        self.assertEqual(s.licenseKeyFormatting("5F3Z-2e-9-w",4), "5F3Z-2E9W")
        self.assertEqual(s.licenseKeyFormatting("2-5g-3-J",2), "2-5G-3J")
        
if __name__ == '__main__':
    unittest.main()
