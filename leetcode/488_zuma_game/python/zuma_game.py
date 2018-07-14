"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won't have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""
import sys
from collections import Counter
class Solution(object):
    def findMinStep(self, board, hand):
        self.ans = sys.maxint
        self.init_len_of_hand = len(hand)
        hand_dict = Counter(hand)

        def helper(board, n, hand_dict):
            if len(board) == 0:
                self.ans = min(self.ans, self.init_len_of_hand - n)
                return
            for i, char in enumerate(board):
                if i > 0 and board[i-1] == char:
                    continue
                j = i
                while j < len(board) and board[j] == char:
                    j += 1
                if j - i >= 3:
                    helper(board[:i] + board[j:], n, hand_dict)
                elif j -i == 2 and hand_dict[char] > 0:
                    hand_dict[char] -= 1
                    helper(board[:i] + board[j:], n-1, hand_dict)
                    hand_dict[char] += 1
                elif hand_dict[char] > 0:
                    hand_dict[char] -= 1
                    helper(board[:i] + char + board[j:], n-1, hand_dict)
                    hand_dict[char] += 1
        helper(board, len(hand), hand_dict)
        return self.ans if self.ans != sys.maxint else -1
