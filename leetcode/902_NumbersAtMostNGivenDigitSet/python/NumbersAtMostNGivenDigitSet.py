class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        lenN = len(str(N))
        totalN = self.getLessLength(D,lenN)  + self.getExactLengh(D, lenN, N)
        return totalN

    def getLessLength(self, D, lenN):
        total = 0
        lenD = len(D)
        for i in range(1,lenN):
            total += pow(lenD, i)
        # print("total : %d" % total)
        return total

    def digitChoice(self, D, digit):
        counter = 0
        for i in D:
            if int(i) <= digit:
                counter += 1
            else:
                break
        return counter

    def getExactLengh(self, D, lenN, N):
        # print("N = %d" % N)
        if N < 10:
            return self.digitChoice(D, N)
        highestDigit = int(str(N)[0])
        # print("highestDigit = %d" % highestDigit)
        if str(highestDigit) not in D:
            higestDigitChoice = self.digitChoice(D, highestDigit)
            return higestDigitChoice * pow(len(D), lenN - 1)
        else:
            higestDigitChoice = self.digitChoice(D, highestDigit)
            # print("higestDigitChoice = %d" % higestDigitChoice)
            part1 =  (higestDigitChoice - 1) * pow(len(D), lenN - 1)
            secondDigit = str(N)[1]
            part2 = 0
            if int(secondDigit) > 0:
                remainedN = int(str(N)[1:]) if N >= 10 else 0
                part2 = self.getExactLengh(D, len(str(remainedN)),remainedN)
            return part1 + part2
