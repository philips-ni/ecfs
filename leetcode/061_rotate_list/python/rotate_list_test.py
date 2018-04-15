
import unittest
import rotate_list

class TestRotate_List(unittest.TestCase):
    def test_rotateRight(self):
        s = rotate_list.Solution()
        l1 = rotate_list.initList([1,2,3,4,5])
        newL = s.rotateRight(l1, 2)
        rotate_list.dump(newL)
        # self.assertEqual(s.rotateRight(), )
if __name__ == '__main__':
    unittest.main()
