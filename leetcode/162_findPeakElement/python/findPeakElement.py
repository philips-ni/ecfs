
class Solution(object):
    def findPeakElement(self, l):
        peaks = []
        for idx in range(len(l)):
            if self.isPeak(l, idx):
                peaks.append(idx)
        return peaks
    
    def isPeak(self, l, idx):
        if idx == len(l) - 1:
            if l[idx] > l[idx-1]:
                return True
        elif idx == 0:
            if l[idx] > l[idx+1]:
                return True
        else:
            if l[idx-1] < l[idx] and l[idx+1] < l[idx]:
                return True
        return False
            

