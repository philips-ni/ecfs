
class Solution(object):
    def largestPerimeter(self, l):
        def detect(l1, l2, l3):
            # print("{} {} {}".format(l1,l2,l3))
            if l1 + l2 > l3:
                return True, sum([l1,l2,l3])
            else:
                return False, 0

        if len(l) < 3:
            return 0
        sorted_l = sorted(l)
        # print(sorted_l)
        i = len(l) - 1
        perimeter = 0
        while i >= 2:
            isTriangle, perimeter = detect(sorted_l[i-2], sorted_l[i-1], sorted_l[i])
            if isTriangle:
                break
            i -= 1
        return perimeter
