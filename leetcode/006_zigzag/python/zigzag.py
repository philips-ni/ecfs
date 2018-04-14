"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
    
    def convert2(self, s, rows):
        """
        :type s: str
        :type numRows: int  (must >= 3)
        :rtype: str
        """
        if s == "":
            return s
        if rows < 2:
            return s
        colums = self.getColums(s,rows)
        # print "colums: %d" % colums
        if colums < 2:
            return s

        matrix = [["" for x in range(colums)] for y in range(rows)]
        for idx in range(0, len(s)):
            c = s[idx]
            posX, posY = self.getPos(idx, rows)
            matrix[posX][posY] = c
        # print matrix
        ret = ""
        for i in range(0,rows):
            for j in range(0,colums):
                if j % 2 == 0:
                    # print "colecting matrix[%d][%d]\n" % (i,j)
                    ret += matrix[i][j]
                else:
                    if rows > 2 :
                        if i != 0 and i != rows - 1:
                            # print "colecting matrix[%d][%d]\n" % (i,j)
                            ret += matrix[i][j]
                    else:
                        if i != rows - 1:
                            ret += matrix[i][j]
        return ret

    def getColums(self, s, rows):
        length = len(s)
        # print "length: %d\n" % length
        if length <= rows:
            return 1
        
        # To make it work for leetcode, generally, "rows < 3" would not be allowed
        if rows == 2:
            m = length / 3
            n = length % 3
            if n == 0:
                return 2 * m
            else:
                return 2 * m  + 1
            
        m = length / (rows + rows - 2)
        n = length % (rows + rows - 2)

        if n == 0:
            return 2 * m
        elif n > rows:
            return 2 * m + 2
        else:
            return 2 * m + 1

    def getPos(self, idx, rows):
        # To make it work for leetcode, generally, "rows < 3" would not be allowed
        # while rows == 2, we only leave the gap in the bottom
        if rows == 2:
            m = (idx + 1) / 3
            n = (idx + 1) % 3
            if n == 0:
                posY = m * 2 -1
                posX = 0
            elif n == 1:
                posY = m * 2
                posX = 0
            else :
                posY = m * 2
                posX = 1
        else:
            m = (idx + 1) / (rows + rows - 2)
            n = (idx + 1) % (rows + rows - 2)
            if n == 0:
                posY = m * 2 - 1
                posX = rows - 2
            elif n > rows:
                posY = m * 2 + 1
                posX = n - rows
            else:
                posY = m * 2
                posX = n - 1
        return posX, posY



