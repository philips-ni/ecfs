
import unittest
import threeSum

class TestThreesum(unittest.TestCase):
    def test_threeSum(self):
        s = threeSum.Solution()

        nlist6 = [0, 0, 0, 1,2,3]
        expectS6 = [[0, 0, 0]]
        self.assertEqual(s.threeSum(nlist6), expectS6)
        
        nlist1 = [-1, 0, 1, 2, -1, -4]
        expectS1 = [
            [-1, -1, 2],
            [-1, 0, 1]
        ]
        self.assertEqual(s.threeSum(nlist1), expectS1)
        nlist2 = []
        expectS2 = []
        self.assertEqual(s.threeSum(nlist2), expectS2)
        nlist3 = [1,-1]
        expectS3 = []
        self.assertEqual(s.threeSum(nlist3), expectS3)
        nlist4 = [1,-1,1]
        expectS4 = []
        self.assertEqual(s.threeSum(nlist4), expectS4)
        nlist5 = [1,-1,1,0]
        expectS5 = [[-1,0,1]]
        self.assertEqual(s.threeSum(nlist5), expectS5)

        nlist5 = [1,-1,2,4,1,-6]
        expectS5 = [[-6,2,4]]
        self.assertEqual(s.threeSum(nlist5), expectS5)

        
        


if __name__ == '__main__':
    unittest.main()
