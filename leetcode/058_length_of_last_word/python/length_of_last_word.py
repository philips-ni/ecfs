
class Solution(object):
    def lengthOfLastWord(self, s):
        length = len(s)
        if length == 0:
            return 0
        endIdx = length - 1
        while endIdx >= 0 and s[endIdx] == " ":
            endIdx -= 1
        if endIdx < 0:
            return 0
        startIdx = endIdx
        while startIdx >= 0 and s[startIdx] != " ":
            startIdx -= 1
        return endIdx - startIdx
