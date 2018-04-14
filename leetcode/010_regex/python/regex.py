"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print "s: %s, len: %d" % (s, len(s))
        # print "p: %s, len: %d" % (p, len(p))

        if len(s) == 0 and len(p) == 0:
            return True
            
        if len(p) == 0 and len(s) != 0:
            return False
            
        if len(p) > 2 and p[1] == "*":
            return self.isMatchStarNotAtEnd(p[0], s, p[2:])

        if len(p) == 2 and p[1] == "*":
            return self.isMatchStarAtEnd(p[0], s)

        if len(s) == 0 and len(p) != 0:
            return False
        
        if p[0] == s[0] or p[0] == ".":
            return self.isMatch(s[1:], p[1:])
        return False
        
    def isMatchStarNotAtEnd(self, c, s, p):
        # print "c: %s" % c
        # print "s: %s" % s
        # print "p: %s" % p
        while True:
            if self.isMatch(s,p):
                return True
            if s == "":
                break
            if c == "." or c == s[0]:
                s = s[1:]
            else:
                break
        return False

    
    def isMatchStarAtEnd(self, c, s):
        # print "c: %s" % c
        # print "s: %s" % s
        if c == ".":
            return True
        for i in range(0,len(s)):
            if s[i] != c:
                return False
        return True
        
                
