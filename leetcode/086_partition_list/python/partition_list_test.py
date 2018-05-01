
import unittest
import partition_list


class TestPartition_List(unittest.TestCase):
    def test_partition(self):
        s = partition_list.Solution()
        l1 = partition_list.initList([1,1])
        l2 = s.partition(l1,0)
        partition_list.dump(l2)
        
        l1 = partition_list.initList([1,4,3,2,5,2,2])
        l2 = s.partition(l1,3)
        partition_list.dump(l2)

        l1 = partition_list.initList([10,1,4,3,2,5,2,2])
        l2 = s.partition(l1,3)
        partition_list.dump(l2)
        
if __name__ == '__main__':
    unittest.main()
