import unittest
import isNStraightHand

class TestIsnstraighthand(unittest.TestCase):
    def test_isNStraightHand(self):
        s = isNStraightHand.Solution()
        hand = [1,2,3,6,2,3,4,7,8]
        self.assertEqual(s.isNStraightHand(hand,3), True)
        hand = [1,2,3,4,5]
        self.assertEqual(s.isNStraightHand(hand,4), False)

        hand = [1]
        self.assertEqual(s.isNStraightHand(hand,1), True) 
        hand = [1,1,2,2,3,3]
        self.assertEqual(s.isNStraightHand(hand,3), True)
       
                
if __name__ == '__main__':
    unittest.main()
