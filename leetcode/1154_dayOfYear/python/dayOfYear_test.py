
import unittest
import dayOfYear

class TestDayofyear(unittest.TestCase):
    def test_dayOfYear(self):
        s = dayOfYear.Solution()
        self.assertEqual(s.dayOfYear("2019-01-09"), 9)
        self.assertEqual(s.dayOfYear("2019-02-10"), 41)
        self.assertEqual(s.dayOfYear("2019-03-01"), 60)
        self.assertEqual(s.dayOfYear("2013-03-01"), 60)        
        self.assertEqual(s.dayOfYear("2004-03-01"), 61)
        
if __name__ == '__main__':
    unittest.main()
