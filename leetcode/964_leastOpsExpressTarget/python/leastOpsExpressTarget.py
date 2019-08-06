from functools import lru_cache
import math
class Solution1(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        print("-" * 80)
        print("x: {}".format(x))
        print("target: {}".format(target))        
        n = int(math.log(target,x))
        print("n: {}".format(n))
        mask = x**n
        print("mask: {}".format(mask))
        
        last = [0,n+1]
        for i in range(n,-1,-1):
            print("i: {}".format(i))            
            print("target: {}".format(target))
            print("mask: {}".format(mask))            
            d = target // mask
            print("d: {}".format(d))
            multis = 2 if i==0 else i
            print("multis: {}".format(multis))                        
            last = [min(last[1]+(x-d)*multis,last[0]+d*multis), min(last[1]+(x-d-1)*multis,last[0]+(d+1)*multis)]
            print("last: {}".format(last))
            target = target % mask
            mask /= x
        return last[0]-1

class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        cost = list(range(40))
        cost[0] = 2

        # @lru_cache(None)
        def dp(i, targ):
            if targ == 0: return 0
            if targ == 1: return cost[i]
            if i >= 39: return float('inf')
            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i+1, t),
                       (x-r) * cost[i] + dp(i+1, t+1))

        return dp(0, target) - 1
