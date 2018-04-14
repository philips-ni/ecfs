import unittest
import firstMissingPositive

class TestFirstmissingpositive(unittest.TestCase):
    def test_firstMissingPositive(self):
        s = firstMissingPositive.Solution()
        self.assertEqual(s.firstMissingPositive([1]),2)                
        self.assertEqual(s.firstMissingPositive([1,2,0]),3 )
        self.assertEqual(s.firstMissingPositive([3,4,-1,1]),2 )

        
if __name__ == '__main__':
    unittest.main()
