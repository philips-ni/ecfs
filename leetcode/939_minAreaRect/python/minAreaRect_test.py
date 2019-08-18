
import unittest
import minAreaRect

class TestMinarearect(unittest.TestCase):
    def test_minAreaRect(self):
        s = minAreaRect.Solution()
        self.assertEqual(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]), 4)
        self.assertEqual(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]), 2)
        self.assertEqual(s.minAreaRect([[1,1]]), 0)
        self.assertEqual(s.minAreaRect([[1,1],[1,2],[2,2],[2,1],[3,2]]), 1)        
                         
if __name__ == '__main__':
    unittest.main()
