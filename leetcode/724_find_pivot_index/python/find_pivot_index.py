
class Solution(object):
    def pivotIndex(self, l):
        sl = []
        s = 0
        for i in l:
            s += i
            sl.append(s)
        for i in range(0, len(l)):
            if i > 0:
                s_left = sl[i-1]
                s_right = sl[len(l) - 1] - sl[i]
            elif i == 0:
                s_left = 0
                s_right = sl[len(l) - 1] - sl[i]
            if s_left == s_right:
                return i
        return -1
