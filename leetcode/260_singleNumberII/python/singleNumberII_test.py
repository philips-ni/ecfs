
import unittest
import singleNumberII

class TestSinglenumberii(unittest.TestCase):
    def test_singleNumber(self):
        s = singleNumberII.Solution()
        self.assertEqual(s.singleNumber([1,2,1,3,2,5]), [3,5])
if __name__ == '__main__':
    unittest.main()
