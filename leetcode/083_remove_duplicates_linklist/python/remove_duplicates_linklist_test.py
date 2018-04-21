import unittest
import remove_duplicates_linklist

class TestRemove_Duplicates_Linklist(unittest.TestCase):
    def test_deleteDuplicates(self):
        s = remove_duplicates_linklist.Solution()
        l1 = remove_duplicates_linklist.initList([1,1,2])        
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist.dump(l2)

        l1 = remove_duplicates_linklist.initList([1,1,2,3,3,3,4,4])        
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist.dump(l2)

        l1 = remove_duplicates_linklist.initList([1])        
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist.dump(l2)

        l1 = remove_duplicates_linklist.initList([])        
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist.dump(l2)
        
if __name__ == '__main__':
    unittest.main()
