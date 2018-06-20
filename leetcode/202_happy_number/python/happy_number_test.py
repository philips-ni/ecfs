
import unittest
import happy_number

class TestHappy_Number(unittest.TestCase):
    def test_isHappy(self):
        s = happy_number.Solution()
        self.assertEqual(s.isHappy(19), True)
        self.assertEqual(s.isHappy(20), False)        
if __name__ == '__main__':
    unittest.main()
