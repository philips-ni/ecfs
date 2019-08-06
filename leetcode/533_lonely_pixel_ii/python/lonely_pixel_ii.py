
class Solution(object):
    def findBlackPixel(self, picture, N):
        count = 0
        rotated_N = zip(*picture)
        print(rotated_N)
        for c in rotated_N:
            if c.count('B') != N: continue
            first_row = picture[c.index('B')]
            if first_row.count('B') != N: continue
            if picture.count(first_row) != N: continue
            count += 1
        return count*N
