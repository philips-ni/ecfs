class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.words_dict = {}
        for idx in range(len(words)):
            if words[idx] not in self.words_dict:
                self.words_dict[words[idx]] = [idx]
            else:
                self.words_dict[words[idx]].append(idx)
        print(self.words_dict)
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortest = float("inf")
        idxs_word1 = self.words_dict[word1]
        idxs_word2 = self.words_dict[word2]

        for idx1 in idxs_word1:
            for idx2 in idxs_word2:
                shortest = min(abs(idx2-idx1), shortest)
        return shortest
                    

