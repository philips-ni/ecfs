
import unittest
import subsets2

class TestSubsets2(unittest.TestCase):
    def test_subsetsWithDup(self):
        s = subsets2.Solution()
        r = s.subsetsWithDup([1,2,2])
        print r

        r = s.subsetsWithDup([4,4,4,1,4])
        print r
        
        
if __name__ == '__main__':
    unittest.main()
