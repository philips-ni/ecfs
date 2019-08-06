
import unittest
import shortest_word_distance

class TestShortest_Word_Distance(unittest.TestCase):
    def test_shortest(self):
        l = ["practice", "makes", "perfect", "coding", "makes"]
        s = shortest_word_distance.WordDistance(l)
        self.assertEqual(s.shortest("coding","practice"), 3)
        self.assertEqual(s.shortest("makes","coding"), 1)
        l = ["a","a","b","b"]
        s = shortest_word_distance.WordDistance(l)        
        self.assertEqual(s.shortest("a","b"), 1)
        self.assertEqual(s.shortest("b","a"), 1)                
if __name__ == '__main__':
    unittest.main()
