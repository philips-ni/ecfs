import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        s = [el * -1 for el in stones]
        heapq.heapify(s)
        while len(s) > 1:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            if a != b:
                heapq.heappush(s, -1 * abs(b-a))
        if len(s) == 0:
            return 0
        else:
            return -1 * s[0]
