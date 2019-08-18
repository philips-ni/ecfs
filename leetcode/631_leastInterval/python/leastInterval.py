import collections
class Solution2:
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        mostOccurence = max([value for value in counter.values()])
        numOfKeys = len([key for key in counter if counter[key] == mostOccurence])
        gapCount = mostOccurence - 1
        gapLength = n - (numOfKeys - 1)
        emptySlots = gapCount * gapLength
        availableTasks = len(tasks) - numOfKeys*mostOccurence
        idles = max(0, emptySlots - availableTasks)
        return idles + len(tasks)
    
class Solution:
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        maxCount = max(counter.values())
        numMax = list(counter.values()).count(maxCount)
        total = (maxCount - 1) * (n + 1) + numMax
        result = max(len(tasks), total)
        return result
