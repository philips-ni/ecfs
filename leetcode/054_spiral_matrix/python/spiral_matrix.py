"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        a = 0
        b = 0
        c = len(matrix) - 1
        d = len(matrix[0]) - 1
        res = []
        while a <= c and b <= d:
            
            for i in range(b, d+1):
                res.append(matrix[a][i])
            a += 1
            
            for i in range(a, c + 1):
                res.append(matrix[i][d])
            d -= 1
            
            if d >= b and a <= c:
                for i in range(d, b-1, -1):
                    res.append(matrix[c][i])
                c -= 1
                for i in range(c, a-1, -1):
                    res.append(matrix[i][b])
                b += 1
        return res


    def spiralOrder2(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        
        n = len(matrix[0])
        
        if n == 0:
            return []
        if m == 1 and n==1:
            return [matrix[0][0]]
        if m == 1:
            return matrix[0]
        if n == 1:
            return [item[0] for item in matrix] 
        
        return [matrix[0][j] for j in range(n-1)] + \
            [matrix[i][n-1] for i in range(m-1)] + \
            [matrix[m-1][j] for j in range(n-1,0,-1)] + \
            [matrix[i][0] for i in range(m-1,0,-1)] + \
            self.spiralOrder([[matrix[i][j] for j in range(1,n-1)] for i in range(1,m-1)])
