from collections import defaultdict
class Solution(object):
    def anagramMappings(self, A, B):
        b_idx_val_dict = defaultdict(dict)
        for idx, v in enumerate(B):
            if v not in b_idx_val_dict:
                b_idx_val_dict[v] = [idx]
            else:
                b_idx_val_dict[v].append(idx)
        ret = []
        for item in A:
            idx = b_idx_val_dict[item].pop(0)
            ret.append(idx)
        return ret
