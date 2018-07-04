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


    def partition(self, l, start, end):
        pivot = l[start]
        i, j = start-1, end+1
        while True:
            i += 1
            j -= 1
            while(l[i] < pivot): i+= 1
            while(l[j] > pivot ): j-= 1
            if i >= j: 
                return j
            l[i], l[j] = l[j], l[i]
