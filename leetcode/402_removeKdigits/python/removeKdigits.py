import itertools
import re
class Solution2(object):
    def removeKdigits(self, num, k):
        if k == 0:
            return num
        if k == len(num):
            return "0"
        ret = num
        for i in range(k):
            ret = self.removeOneDigit(ret)
        return ret
    
    def removeOneDigit(self,num):
        if len(num) == 1:
            return "0"
        if len(num) > 2 and num[1] == 0:
            return str(num[2:])
        t = int(num)
        for i in range(len(num)):
            t = min(t, int(num[0:i] + num[i+1:]))
        return str(t)

class Solution1(object):
    def removeKdigits(self, num, k):
        print("num: {}".format(num))
        res = []
        if len(num) == k:
            return '0'
        for i in range(len(num)):
            # Monotone Stack
            while res and k and res[-1] > num[i]:
                res.pop()
                k -= 1
            res.append(num[i])
            print("i: {}, res:{}".format(i,res))            
        print(res)
        ret = ''.join(res)
        # removing the leading 0s
        ret = re.sub(r'^0+', '', ret)[]
        if ret == '':
            ret = '0'
        else:
            ret = ret[0 : -1 * k]
        return ret

class Solution2(object):
    def removeKdigits(self, num, k):
        res = []
        for i in range(len(num)):
            while res and k and res[-1] > num[i]:
                res.pop()
                k -= 1
            res.append(num[i])
        print(res)        
        start = next((i for i, n in enumerate(res) if n != '0'), len(res))
        # print(start)
        ret = ''.join(n for n in itertools.islice(res, start, len(res) - k)) or '0'
        # print(ret)
        return ret
    

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for i in range(len(num)):
            # Monotone Stack            
            while k>0 and result and num[i] < result[-1]:
                result.pop()
                k-=1
            result.append(num[i])
        if k > 0:
            result = result[:len(result)-k]
        result = ''.join(result).lstrip('0')

        return result if result!="" else '0'    
