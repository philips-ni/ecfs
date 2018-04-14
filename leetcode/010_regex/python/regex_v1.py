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
        # print "s: %s" % s
        # print "p: %s" % p

        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) == 0 or len(p) == 0:
            return False
        states = self.getStates(p)
        print "states : %s" % states
        stIdx = 0
        sIdx = 0
        while( sIdx < len(s) and stIdx < len(states)):
            print "sIdx : %d" % sIdx
            print "stIdx : %d" % stIdx
            if self.match(s[sIdx], states[stIdx]):
                if sIdx < len(s) - 1 and \
                   stIdx < len(states) - 1 and \
                   self.isStarState(states[stIdx]) and \
                   s[sIdx + 1] == s[sIdx] and \
                   s[sIdx + 1] == states[stIdx + 1][0]:
                    sIdx + =1
                elif sIdx < len(s) - 1 and \
                   stIdx < len(states) - 1 and \
                   self.isStarState(states[stIdx]) and \
                   s[sIdx + 1] == states[stIdx + 1][0]:
                    sIdx += 1
                    stIdx += 1
                elif self.isStarState(states[stIdx]):
                    sIdx += 1
                else:
                    sIdx += 1
                    stIdx += 1
            elif self.isStarState(states[stIdx]):
                stIdx += 1
            else:
                break
        print "out sIdx : %d" % sIdx
        print "out stIdx : %d" % stIdx
        if sIdx == len(s) :
            if stIdx == len(states) - 1 and self.isStarState(states[stIdx]):
                return True
            elif stIdx == len(states):
                return True
            else:
                return False
        else:
            return False


    def getStates(self, p):
        states = []
        preState= p[0]
        for idx in range(1, len(p)):
            if p[idx] == "*":
               preState = preState + p[idx]
            else:
                state = preState
                preState = p[idx]
                states.append(state)
        states.append(preState)
        return states
                

    def isStarState(self, state):
        if state[-1] == "*":
            return True
        else:
            return False

    def match(self, c, state):
        if state[0] == '.':
            return True
        if state[0] == c:
            return True
        else:
            return False
        
