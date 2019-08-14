
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        my_pos = [0,0]
        my_distance = distance(my_pos, target)
        print("my_distance: {}".format(my_distance))
        ret = True
        for g in ghosts:
            if distance(g, target) <= my_distance:
                ret = False
                break
        return ret
            
