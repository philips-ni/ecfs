# Given an array of integers find all pairs whose sum is zero,
# please make sure each item can only be used once
#
# Example: {1,-1,-1,2,-2,2,-2,4,-4,0,0,0,0} =>
# (1,-1),(2,-2),(4,-4),(0,0),(0,0),(2,-2)
from collections import defaultdict
def findSumZeroPairs2(l):
    # l: list
    # retType: list of a tuple, such as [(1,-1),...]
    val_idx_dict = defaultdict(list)
    idx_visited_dict = defaultdict(lambda : False)
    for idx, v in enumerate(l):
        val_idx_dict[v].append(idx)
    # print(val_idx_dict)
    retl = []
    for i, v in enumerate(l):
        another_part = 0 - v
        if not idx_visited_dict[i] and another_part in val_idx_dict and \
               len(val_idx_dict[another_part]) > 0 and \
               not idx_visited_dict[val_idx_dict[another_part][0]]:
            if v != 0:
                retl.append((v, another_part))
                idx_visited_dict[i] = True
                idx_visited_dict[val_idx_dict[another_part][0]] = True
                val_idx_dict[another_part] = val_idx_dict[another_part][1:]
            else:
                if len(val_idx_dict[0]) < 2:
                    continue
                else:
                    retl.append((v, another_part))
                    idx_visited_dict[i] = True
                    idx_visited_dict[val_idx_dict[another_part][1]] = True
                    val_idx_dict[another_part] = val_idx_dict[another_part][2:]
    return retl

retl = findSumZeroPairs2([1,1,-1,-1,2,-2,2,-2,4,-4,0,0,0,0])
print(retl)
retl = findSumZeroPairs2([1,-1,1,-1,-1,2,1,-2])
print(retl)

# bash-3.2$ python findSumZeroPairs2.py
# [(1, -1), (1, -1), (2, -2), (2, -2), (4, -4), (0, 0), (0, 0)]
# [(1, -1), (1, -1), (2, -2), (1, -1)]
# bash-3.2$
# 
