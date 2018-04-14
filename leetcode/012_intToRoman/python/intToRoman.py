"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanN = ""
        iterN = num
        deepLevel = 0
        while iterN > 0:
            remainder = iterN % 10
            romanN = self.convert(remainder, deepLevel) + romanN
            iterN = iterN / 10
            deepLevel += 1
        return romanN

    def convert(self, n, level):
        # print "n: %d" % n
        # print "level  %d" % level
        oneUnit = ['I','X','C','M','N/A']
        fiveUnit = ['V','L','D', 'N/A']
        
        firstNineNums = ["N/A", "I","II","III","IV","V","VI","VII","VIII","IX"]
        
        iPair = oneUnit[level]
        vPair = fiveUnit[level]
        xPair = oneUnit[level + 1]
        basicN = firstNineNums[n]
        romanN = ""
        for i in range(0, len(basicN)):
            if basicN[i] == "I" :
                romanN += iPair
            elif basicN[i] == "V":
                romanN += vPair
            elif basicN[i] == "X":
                romanN += xPair
            else:
                pass # will not come here
        # print romanN
        return romanN
