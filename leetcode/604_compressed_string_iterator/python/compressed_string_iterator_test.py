
import unittest
from  compressed_string_iterator import StringIterator

class TestCompressed_String_Iterator(unittest.TestCase):
    def test_StringIterator(self):
        compressedString = "L1e2t2"
        obj = StringIterator(compressedString)
        self.assertEqual(obj.next(), 'L')
        self.assertEqual(obj.next(), 'e')
        self.assertEqual(obj.next(), 'e')
        self.assertEqual(obj.next(), 't')
        self.assertEqual(obj.hasNext(), True)                
        self.assertEqual(obj.next(), 't')
        self.assertEqual(obj.hasNext(), False)        
        
if __name__ == '__main__':
    unittest.main()
