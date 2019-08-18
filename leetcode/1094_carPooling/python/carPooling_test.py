
import unittest
import carPooling

class TestCarpooling(unittest.TestCase):
    def test_carPooling(self):
        s = carPooling.Solution()
        trips = [[2,1,5],[3,3,7]]
        capacity = 4
        # self.assertEqual(s.carPooling(trips, capacity), False)
        trips = [[2,1,5],[3,3,7]]
        capacity = 5
        # self.assertEqual(s.carPooling(trips, capacity), True)
        trips = [[2,1,5],[3,5,7]]
        capacity = 3
        # self.assertEqual(s.carPooling(trips, capacity), True)        
        trips = [[3,2,7],[3,7,9],[8,3,9]]
        capacity = 11
        # self.assertEqual(s.carPooling(trips, capacity), True)
        trips = [[2,2,6],[2,4,7],[8,6,7]]
        capacity = 11
        self.assertEqual(s.carPooling(trips, capacity), True)        
if __name__ == '__main__':
    unittest.main()
