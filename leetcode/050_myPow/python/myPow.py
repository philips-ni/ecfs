"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""
class Solution(object):
    def myPow2(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n > 1:
            if n % 2 == 0:
                tmp = self.myPow(x, n/2)
                return tmp * tmp
            else:
                tmp = self.myPow(x, n/2)
                return tmp * tmp * x
        else:
            return 1.0 / self.myPow(x, -1 * n)

    def myPow(self, x, n):
        m = -n if n < 0 else n
        y = 1
        while m:
#             print "before m: %d" % m
#             print "before x: %d" % x
#             print "before y: %d" % y                        
            if m % 2 == 1:
                y *= x
            x *= x
            m = m / 2
#             print "after m: %d" % m
#             print "after x: %d" % x
#             print "after y: %d" % y                        
            
        return y if n >= 0 else 1.0 / y        
