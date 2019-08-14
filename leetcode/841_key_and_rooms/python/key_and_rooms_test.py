
import unittest
import key_and_rooms

class TestKey_And_Rooms(unittest.TestCase):
    def test_canVisitAllRooms(self):
        s = key_and_rooms.Solution()
        self.assertEqual(s.canVisitAllRooms([[1],[2],[3],[]]), True )
        self.assertEqual(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]), False)
if __name__ == '__main__':
    unittest.main()
