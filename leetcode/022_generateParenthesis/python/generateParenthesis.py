class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
        l = []
        left = n
        right = n
        s = ""
        self._gen(l, left, right, s)
        return l

    def _gen(self, l, left, right, s):
        if right < left:
            return
        if left == 0 and right == 0:
            l.append(s)
            return
        if left > 0:
            self._gen(l, left -1, right, s + "(")
        if right > 0:
            self._gen(l, left, right -1, s + ")")
        
