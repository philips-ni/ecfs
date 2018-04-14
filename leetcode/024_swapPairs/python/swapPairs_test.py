
import unittest
import swapPairs

class TestSwappairs(unittest.TestCase):
    def test_swapPairs(self):
        s = swapPairs.Solution()
        l1 = swapPairs.initList([1,2,4,5])        
        l2 = s.swapPairs(l1)
        swapPairs.dump(l2)

        l1 = swapPairs.initList([1])        
        l2 = s.swapPairs(l1)
        swapPairs.dump(l2)

        l1 = swapPairs.initList([1,2,4,5,3])        
        l2 = s.swapPairs(l1)
        swapPairs.dump(l2)
        
if __name__ == '__main__':
    unittest.main()
