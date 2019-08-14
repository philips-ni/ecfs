# sieve of Eratosthenes 
import math
class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        prime = [ True for _ in range(n)]
        prime[0] = prime[1] = False
        
        p = 2
        while p * p < n:
            if prime[p] == True:
                for i in range(p*p, n, p):
                    prime[i] = False
            p += 1
        ret = 0
        for el in prime:
            if el == True:
                ret += 1
        return ret
        
