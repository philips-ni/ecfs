
class Solution(object):
    def bit_add(self, a, b):
        while b != 0:
            a1 = a ^ b
            b1 = (a & b) << 1
            a = a1
            b = b1
        return a
    
    def bit_minus(self, a, b):
        minus_b = self.bit_add(~b, 1)
        return self.bit_add(a,minus_b)
