
import unittest
import sortByCategory

class TestSortbycategory(unittest.TestCase):
    def test_sortByCategory(self):
        s = sortByCategory.Solution()
        
        # 2 1 3 5 7 9 6
        # H M H L M L M

        cat_dict = { 2: 'H',
                     1: 'M',
                     3: 'H',
                     5: 'L',
                     7: 'M',
                     9: 'L',
                     6: 'M'
                    }
        print cat_dict
        l = [2,1,3,5,7,9,6]
        s.sortByCategory(l, cat_dict)
        print l
        self.assertEqual(l,[5,9,1,7,6,2,3])
if __name__ == '__main__':
    unittest.main()
