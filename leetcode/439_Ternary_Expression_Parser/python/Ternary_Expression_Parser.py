
class Solution(object):
    def parseTernary(self, expression):
        balance = -1
        sep_idx = 0
        if len(expression) == 1:
            return expression[0]
        for i in range(3, len(expression)):
            if expression[i] == '?':
                balance -= 1
            elif expression[i] == ':':
                balance += 1
            if balance == 0:
                sep_idx = i
                break
        if expression[0] == 'T':
            return self.parseTernary(expression[2:sep_idx])
        else:
            return self.parseTernary(expression[sep_idx + 1:])
            
