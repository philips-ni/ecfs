# Given an array of integers find all uniqe pairs whose sum is zero
#
# Example: {1,2,-1,10,0,-3,-2,5,-5,4,4,4,-4,1} =>
# (1,-1),(2,-2),(5,-5),(4,-4)
# Please notice, we treat (1,-1) is the same pair as (-1,1)

from collections import defaultdict
def findSumZeroPairs(l):
    # l: list
    # retType: list of a turple, such as [(1,-1),...]
    val_idx_dict = defaultdict(list)
    for idx, v in enumerate(l):
        val_idx_dict[v].append(idx)
    # print(val_idx_dict)
    retl = set([])
    for i in l:
        another_part = 0 - i
        if i == 0 and len(val_idx_dict[i]) < 2:
            continue
        if another_part in val_idx_dict:
            if not isIncluded(retl, (i, another_part)):
                retl.add((i,another_part))
    return list(retl)

def isIncluded(l, pair):
    n1,n2 = pair
    # print("n1:{},n2:{}".format(n1,n2))
    return pair in l or (n2,n1) in l

retl = findSumZeroPairs([1,2,-1,10,0,-3,-2,5,-5,4,4,4,-4,1])
print(retl)

#  bash-3.2$ ppython findSumZeroPairs.py
#  [(1,-1), (2, -2), (5, -5), (4, -4)]
#
