"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

"""
class Solution {
public:
    int numDecodings(string s) {
        vector<int> memo(s.length(), -1);
        return helper(s, memo, 0);
    }
    
    int helper(string &s, vector<int> &memo, int i)
    {
        if(i>=s.length())
            return 1;
        if(memo[i]>=0)
            return memo[i];
        int r = 0;
        if (s[i] != '0')
            r += helper(s, memo, i+1);
        if(i < s.length() - 1 && ((s[i] == '2' && s[i+1]<'7') || s[i]=='1'))
            r+= helper(s, memo, i+2);
        memo[i] = r;
        return memo[i];
    }
};
"""
class Solution(object):
    def numDecodings(self, s):
        memo = [-1] * len(s)
        return self._numDecodings(s, memo, 0)

    def _numDecodings(self,s, memo, i):
        if i >= len(s):
            return 1
        if memo[i] > 0:
            return memo[i]
        ret = 0
        if s[i] != '0':
            ret += self._numDecodings(s, memo, i+1)
        if i < len(s) - 1 and (( s[i] == '2' and s[i+1] < '7') or s[i] == '1'):
            ret += self._numDecodings(s, memo, i+2)
        memo[i] = ret
        return memo[i]
    
    def numDecodings2(self, s):
        comps = self.getComps(s)
        print comps
        counter = 0
        for comp in comps:
            if self.isValidComp(comp):
                counter += 1
        return counter
    
    def getComps(self, s):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        tmp = self.getComps(s[:-1])
        ret = []
        for item in tmp:
            merged = self.merge(item, s[-1])
            for m in merged:
                ret.append(m)
        return ret
                       
    def merge(self, item, c):
        ret = [item + [c]]
        if len(item[-1]) == 1:
            x = item[-1] + c
            item[-1] = x
            ret.append(item)
        return ret
    
    def isValidComp(self, comp):
        for i in comp:
            if len(i) > 1 and i[0] == "0":
                return False
            if int(i) > 26 or int(i) < 1:
                return False
        return True                
