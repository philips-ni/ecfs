class Solution(object):
    def minMutation(self, start, end, bank):
        step = [len(bank)]
        exist = [False]
        def dfs(el, bank, count):
            if el == end:
                step[0] = min(step[0], count)
                exist[0] = True
                return
            elif count > step[0]:
                return

            for b in range(len(bank)):
                diff = 0
                for i in range(8):
                    if bank[b][i] != el[i]:
                        diff += 1
                        if diff == 2:
                            break
                if diff == 1:
                    temp = bank.pop(b)
                    dfs(temp, bank[:], count + 1)
                    bank.insert(b, temp)
        dfs(start, bank[:], 0)
        return step[0] if exist[0] else -1
        

        
