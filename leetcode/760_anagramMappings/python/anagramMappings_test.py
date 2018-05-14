import unittest
import anagramMappings

class TestAnagrammappings(unittest.TestCase):
    def test_anagramMappings(self):
        s = anagramMappings.Solution()
        a = [12, 28, 46, 32, 50]
        b = [50, 12, 32, 46, 28]
        self.assertEqual(s.anagramMappings(a, b), [1, 4, 3, 2, 0])

        a = [12, 28, 46, 32, 50, 12]
        b = [50, 12, 32, 46, 28, 12]
        self.assertEqual(s.anagramMappings(a, b), [1, 4, 3, 2, 0, 5])
        
if __name__ == '__main__':
    unittest.main()
