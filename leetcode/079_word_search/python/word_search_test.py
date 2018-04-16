
import unittest
import word_search

class TestWord_Search(unittest.TestCase):
    def test_exist(self):
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]
        s = word_search.Solution()
        # self.assertEqual(s.exist(board, "ABCCED"), True )
        self.assertEqual(s.exist(board, "SEE"), True )
        # self.assertEqual(s.exist(board, "ABCB"), False )
        
if __name__ == '__main__':
    unittest.main()
