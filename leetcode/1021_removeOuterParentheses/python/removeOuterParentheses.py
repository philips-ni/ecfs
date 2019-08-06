class Solution(object):
    def removeOuterParentheses(self, S):
        ret = ""
        stack = []
        start = end = 0
        for i in range(len(S)):
            if S[i] == "(":
                if len(stack) == 0:
                    start = i
                stack.append(S[i])
            elif S[i] == ")":
                stack.pop()
                if len(stack) == 0:
                    end = i
                    ret += S[start+1:end]
            else:
                assert False
        return ret
                    
            
