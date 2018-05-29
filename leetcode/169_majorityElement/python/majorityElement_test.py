
import unittest
import majorityElement

class TestMajorityelement(unittest.TestCase):
    def test_majorityElement(self):
        s = majorityElement.Solution()
        self.assertEqual(s.majorityElement([2,2,1,1,1,2,2]),2 )
        self.assertEqual(s.majorityElement([3,2,3]),3)
if __name__ == '__main__':
    unittest.main()
