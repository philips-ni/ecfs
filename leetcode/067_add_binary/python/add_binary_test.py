
import unittest
import add_binary

class TestAdd_Binary(unittest.TestCase):
    def test_addBinary(self):
        s = add_binary.Solution()
        self.assertEqual(s.addBinary("11","1"), "100" )
        self.assertEqual(s.addBinary("101","1"), "110" )
        self.assertEqual(s.addBinary("101","11"), "1000")
        
if __name__ == '__main__':
    unittest.main()
