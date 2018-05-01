class Solution(object):
    def rotate(self, m):
        n = len(m)
        if n == 0:
            return
        m[::] = m[::-1]
        for i in range(0, n):
            for j in range(i+1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]                

    def rotate2(self, matrix):
        matrix[::] = list(zip(*matrix[::-1]))
        
                
