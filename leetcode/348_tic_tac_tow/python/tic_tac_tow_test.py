import unittest
import tic_tac_tow

class TestTic_Tac_Tow(unittest.TestCase):
    def test_TicTacToe(self):
        s = tic_tac_tow.TicTacToe(3)
        self.assertEqual(s.move(0,0,1), 0)
        self.assertEqual(s.move(0,2,2), 0)
        self.assertEqual(s.move(2,2,1), 0)
        self.assertEqual(s.move(1,1,2), 0)
        self.assertEqual(s.move(2,0,1), 0)
        self.assertEqual(s.move(1,0,2), 0)                
        self.assertEqual(s.move(2,1,1), 1)

        s = tic_tac_tow.TicTacToe(2)
        self.assertEqual(s.move(0,1,1), 0)
        self.assertEqual(s.move(1,1,2), 0)
        self.assertEqual(s.move(1,0,1), 1)
                
        
if __name__ == '__main__':
    unittest.main()
