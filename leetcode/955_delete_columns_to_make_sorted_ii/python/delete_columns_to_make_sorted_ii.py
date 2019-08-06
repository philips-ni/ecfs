from copy import copy

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A_len, str_len, res = len(A), len(A[0]), 0
        is_need_compare = [True] * A_len
        print("-" * 80)
        for col in xrange(str_len):
            tmp = copy(is_need_compare)
            for row in xrange(1, A_len):
                print("row: {}, col: {}, is_need_compare: {}".format(row, col,is_need_compare))
                if is_need_compare[row]:
                    if A[row][col] < A[row - 1][col]:
                        print("need del, row: {}, col: {}".format(row,col))
                        res += 1
                        is_need_compare = tmp
                        print(is_need_compare)
                        break

                    elif A[row][col] > A[row - 1][col]:
                        print("no need del, row: {}, col: {}".format(row,col))
                        is_need_compare[row] = False
                    else:
                        # still need compare
                        pass
                            
        return res
