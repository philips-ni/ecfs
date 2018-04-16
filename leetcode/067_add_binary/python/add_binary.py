"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution(object):
    def addBinary(self, s1, s2):
        lenOfS1 = len(s1)
        lenOfS2 = len(s2)
        iterS1 = lenOfS1 - 1
        iterS2 = lenOfS2 - 1
        carry = 0
        ret = ""
        while iterS1 >= 0 or iterS2 >=0:
            currS1 = 0 if iterS1 < 0 else s1[iterS1]
            currS2 = 0 if iterS2 < 0 else s2[iterS2]
#             print "iterS1: %d" % iterS1
#             print "iterS2: %d" % iterS2
#             print "currS1: <%s>" % currS1            
#             print "currS2: <%s>" % currS2
#             print "carry: %d" % carry
            if carry == 0:
                if int(currS1) == int(currS2):
                    ret = "0" + ret
                    carry = 0
                    if currS1 == "1":
                        carry = 1
                else:
                    ret = "1" + ret
            else:
                if int(currS1) == int(currS2):
                    ret = "1" + ret
                    carry = 0
                    if currS1 == "1":
                        carry = 1
                else:
                    ret = "0" + ret
                    carry = 1
            iterS1 -= 1
            iterS2 -= 1
        if carry == 1:
            ret = "1" + ret
        return ret
    
            
        
    
