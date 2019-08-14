import itertools
class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        self.S = S[1:-1]
        N = len(self.S)
        ans = []
        for i in range(1, N):
            first = self.make(0,i)
            if len(first) == 0:
                continue
            second = self.make(i,N)
            if len(second) == 0:
                continue
            ans += ["({}, {})".format(*cand) for cand in itertools.product(first, second)]
        return ans
            
    def make(self, i, j):
        ans = []
        for d in range(i+1, j+1):
            left, right = self.S[i:d], self.S[d:j]
            if (not left.startswith('0') or left == '0') and (not right.endswith('0')):
                ans.append(left + ('.' if d != j else '') + right)
        # print("i: {}, j: {}".format(i,j))
        # print("ans: {}".format(ans))
        return ans
