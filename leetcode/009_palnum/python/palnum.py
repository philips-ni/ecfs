"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        isPalFlag = True
        if x < 0 :
            return False
        iterX = x
        while iterX >= 10:
            # print "iterX 1 : %d" % iterX
            len = self.getNumLen(iterX)
            leftmost = iterX / pow(10, len-1)
            rightmost = iterX  % 10
            # print "leftmost : %d" % leftmost
            # print "rightmost : %d" % rightmost
            if leftmost != rightmost:
                isPalFlag = False
                break
            iterX = self.getNextRoundX(iterX)
            # print "iterX 2 : %d" % iterX
            newLen = self.getNumLen(iterX)
            # print "len : %d" % len
            # print "newLen : %d" % newLen
            # To deal with multiple 0 in the middle of num
            if (len - newLen) > 2 :
                gap = pow(10, len - newLen -2)
                if iterX % gap  != 0:
                    isPalFlag = False
                    break
                else:
                    iterX = iterX / gap
                    # print "iterX 3 : %d" % iterX
        return isPalFlag

    def getNextRoundX(self,x):
        """
        convert 23432 to 343
        """
        len = self.getNumLen(x)
        leftmost = x / pow(10, len-1)
        newX = (x - leftmost * pow(10,len -1)) / 10
        return newX

    def getNumLen(self, x):
        len = 0
        iterX = x
        while iterX > 0:
            iterX = iterX / 10
            len += 1
        return len
        
