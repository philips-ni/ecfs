
import unittest
import reorder_list

class TestReorder_List(unittest.TestCase):
    def test_reorderList(self):
        s = reorder_list.Solution()
        l1 = reorder_list.initList([1,2,3,4])
        reorder_list.dump(l1)        
        s.reorderList(l1)
        reorder_list.dump(l1)

        l1 = reorder_list.initList([1,2,3,4,5])
        reorder_list.dump(l1)        
        s.reorderList(l1)
        reorder_list.dump(l1)
        
if __name__ == '__main__':
    unittest.main()
