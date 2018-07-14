import random
class Solution(object):
    def quick_sort(self, l):
        if len(l) < 2:
            return
        else:
            self._quick_sort(l, 0, len(l) - 1)

    def _quick_sort(self,l, start, end):
        if start < end:
            pos = self.partition(l,start, end)
            self._quick_sort(l,start,pos-1)
            self._quick_sort(l,pos+1, end)


    def partition( self, l, start, end ) :
        pivot = start + random.randrange( end - start + 1 )
        l[pivot],l[end] = l[end], l[pivot]
        for i in range( start, end ):
            if l[i] <= l[end]:
                l[i],l[start] = l[start],l[i]
                start += 1
        l[start],l[end] = l[end],l[start]
        return start
