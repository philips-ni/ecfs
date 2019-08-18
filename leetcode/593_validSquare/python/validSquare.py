from collections import Counter
class Solution(object):
    def validSquare(self, p1,p2,p3,p4):
        points = [p1,p2,p3,p4]
        distancesSquare = []
        # Get all disanances's square between each point
        for i in range(3):
            for j in range(i+1, 4):
                distancesSquare.append(self.getDistanceSquare(points[i], points[j]))
        counter = Counter(distancesSquare)
        # for a squre, it has to have 4 equal length side and 2 qual length  diagona
        if sorted(counter.values()) != [2,4]:
            return False
        diagonalSquare = max(counter.keys())
        sideSquare = min(counter.keys())
        # for a squre, diagonalSquare should already be double of sideSquare
        if diagonalSquare != 2 * sideSquare:
            return False
        return True

    def getDistanceSquare(self, p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        return pow((y2-y1),2) + pow( (x2-x1), 2)
            
                                 
