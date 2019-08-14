
import unittest
import random_pick_index

class TestRandom_Pick_Index(unittest.TestCase):
    def test_pick(self):
        l = [1,2,3,3,3]
        s = random_pick_index.Solution(l)
        ret = s.pick(3)
        self.assertEqual(ret in [2,3,4], True)
        ret = s.pick(1)
        self.assertEqual(ret, 0)

if __name__ == '__main__':
    unittest.main()
