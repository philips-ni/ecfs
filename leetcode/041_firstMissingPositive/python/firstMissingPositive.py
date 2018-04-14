
class Solution(object):
    def firstMissingPositive(self, l):
        length = len(l)
        # helperL will record if from 1 to length of l, which num exists
        # if it exists, helperL[num] will be assigned to 1
        helperL = [0] * length
        for n in l:
            if n > 0 and n <=  length:
                helperL[n - 1] = 1
        print helperL
        idx = 0
        while idx < length:
            if helperL[idx] == 0:
                break
            idx += 1
        return idx + 1
