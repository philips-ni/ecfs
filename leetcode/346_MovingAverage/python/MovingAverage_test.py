import unittest
import MovingAverage

class TestMovingaverage(unittest.TestCase):
    def test_MovingAverage(self):
        m = MovingAverage.MovingAverage1(3)
        self.assertEqual(m.next(1), 1)
        self.assertEqual(m.next(10), 5)
        self.assertEqual(m.next(3), 4)
        self.assertEqual(m.next(5), 6)
if __name__ == '__main__':
    unittest.main()
