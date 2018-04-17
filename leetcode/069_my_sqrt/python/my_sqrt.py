
class Solution(object):
    def mySqrt0(self, n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        possibleS = n / 2
        while (possibleS + 1) * (possibleS + 1) > n:
            if possibleS * possibleS <= n:
                break
            else:
                possibleS = possibleS / 2
        if possibleS * possibleS == n:
            return possibleS
        
        while possibleS * possibleS  < n:
            possibleS += 1
            
        if possibleS * possibleS == n:
            return possibleS
        else:
            return possibleS - 1
        
    def mySqrt(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self._mySqrt(n, 1, n / 2)

    def _mySqrt(self, n, rangeStart, rangeEnd):
        mid = rangeStart + (rangeEnd - rangeStart) / 2
        tmp1 = mid * mid
        tmp2 = (mid + 1)  * (mid + 1)
        if tmp1 == n:
            return mid
        if tmp2 == n:
            return mid + 1
        if tmp1 < n and tmp2 > n:
            return mid
        if tmp2 < n:
            return self._mySqrt(n, mid + 1, rangeEnd)
        else:
            return self._mySqrt(n, rangeStart, mid - 1)
        
        
