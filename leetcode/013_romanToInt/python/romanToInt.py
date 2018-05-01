"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt2(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
    
    def romanToInt(self, romanS):
        """
        :type num: int
        :rtype: str
        """
        ret = 0
        previousLevel = -1
        previousV = 0
        levelV = 0
        idx = 0
        for i in range(0,len(romanS)):
            (v, level) = self.getValueAndLevel(romanS[i])
            if previousLevel == -1 :
                levelV = v
                previousLevel = level
                previousV = v
                if idx == len(romanS) - 1:
                    ret = v * pow(10, level)
                    break
                else:
                    idx += 1                
            elif previousLevel < level:
                if levelV == 1 and v == 1:
                    levelV = 9
                    ret = ret + levelV * pow(10, previousLevel)
                    previousV = 0
                    levelV = 0
                else:
                    return -1
                if idx == len(romanS) - 1:
                    break
                else:
                    idx += 1                
            elif previousLevel > level:
                ret = ret + levelV * pow(10, previousLevel)
                levelV = v
                previousLevel = level
                previousV = v
                if idx == len(romanS) - 1:
                    ret = ret + levelV * pow(10,level)
                    break
                else:
                    idx += 1
            else:    # previousLevel == level
                if v == 5 and previousV == 1:
                    levelV = 4
                elif v == 5 and previousV == 0:
                    levelV = v
                elif v == 1 and (levelV < 3 or levelV in range(5,9)):
                    previousV = 1
                    levelV += 1
                else:
                    return -1

                if idx == len(romanS) - 1:
                    ret = ret + levelV * pow(10,level)
                    break
                else:
                    idx += 1
        return ret


    def getValueAndLevel(self, c):
        dict = {
            "I": (1, 0),
            "V": (5, 0),
            "X": (1, 1),
            "L": (5, 1),
            "C": (1, 2),
            "D": (5, 2),
            "M": (1, 3)
        }
        return dict[c]
        
