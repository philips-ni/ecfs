
import unittest
import removeElement

class TestRemoveelement(unittest.TestCase):
    def test_removeElement(self):
        s = removeElement.Solution()
        l1 = [3,2,2,3,4,3,2]
        
        self.assertEqual(s.removeElement(l1,3), 4)
        self.assertEqual(l1[0], 2)
        self.assertEqual(l1[1], 2)
        self.assertEqual(l1[2], 4)
        self.assertEqual(l1[3], 2)                        

        l2 = [2]
        self.assertEqual(s.removeElement(l2,3), 1)
        self.assertEqual(l2[0], 2)


        l3 = [3,2,2,3,4,3,2,3,3]
        
        self.assertEqual(s.removeElement(l3,3), 4)
        self.assertEqual(l3[0], 2)
        self.assertEqual(l3[1], 2)
        self.assertEqual(l3[2], 4)
        self.assertEqual(l3[3], 2)                                

        l4 = []
        self.assertEqual(s.removeElement(l4,3), 0)


        l5 = [3,3]
        self.assertEqual(s.removeElement(l5,5), 2)
        self.assertEqual(l5[0], 3)
        self.assertEqual(l5[1], 3)        

        
if __name__ == '__main__':
    unittest.main()
