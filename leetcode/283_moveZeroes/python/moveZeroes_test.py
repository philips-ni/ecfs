
import unittest
import moveZeroes

class TestMovezeroes(unittest.TestCase):
    def test_moveZeroes(self):
        s = moveZeroes.Solution()
        l = [0, 1, 0, 3, 12]
        s.moveZeroes(l)
        self.assertEqual(l,[1, 3, 12, 0, 0])

        l = [0]
        s.moveZeroes(l)
        self.assertEqual(l,[0])

        l = [0,0,1,2,3]
        s.moveZeroes(l)
        self.assertEqual(l,[1,2,3,0,0])

        l = [1,2,3,0,0]
        s.moveZeroes(l)
        self.assertEqual(l,[1,2,3,0,0])
        
if __name__ == '__main__':
    unittest.main()
