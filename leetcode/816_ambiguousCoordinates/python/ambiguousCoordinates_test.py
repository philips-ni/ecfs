
import unittest
import ambiguousCoordinates

class TestAmbiguouscoordinates(unittest.TestCase):
    def test_ambiguousCoordinates(self):
        s = ambiguousCoordinates.Solution()
        s.ambiguousCoordinates("(100123)")
        print(s.make(0,3))
        print(s.make(3,6))        
"""        
        self.assertEqual(s.ambiguousCoordinates("(123)"), ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"])
        self.assertEqual(s.ambiguousCoordinates("(00011)"), ["(0.001, 1)", "(0, 0.011)"])
        self.assertEqual(s.ambiguousCoordinates("(0123)"), ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"])
        self.assertEqual(s.ambiguousCoordinates("(100)"), ["(10, 0)"])
"""


        
if __name__ == '__main__':
    unittest.main()
