
import unittest
import remove_duplicates_linklist2

class TestRemove_Duplicates_Linklist2(unittest.TestCase):
    def test_deleteDuplicates(self):
        s = remove_duplicates_linklist2.Solution()

        l1 = remove_duplicates_linklist2.initList([1,2,2])
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist2.dump(l2)

        l1 = remove_duplicates_linklist2.initList([1,1,1,2,3])
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist2.dump(l2)

        l1 = remove_duplicates_linklist2.initList([3,4,4,5])
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist2.dump(l2)

        l1 = remove_duplicates_linklist2.initList([1,2,3,3,4,4,5])
        l2 = s.deleteDuplicates(l1)
        remove_duplicates_linklist2.dump(l2)


        
if __name__ == '__main__':
    unittest.main()
