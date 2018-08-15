
import unittest
import mydb

class TestMydb(unittest.TestCase):
    def test_mydb(self):
        s = mydb.Solution()
        self.assertEqual(s.mydb(), )
if __name__ == '__main__':
    unittest.main()
