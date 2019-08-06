class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [["" for i in range(n)] for j in range(n)]
        self.size = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.judge(row,col,player) != 0:
            print("Game is over, no more move allowed")
            sys.exit(-1)
        if player == 1:
            self.board[row][col] = "X"
        elif player == 2:
            self.board[row][col] = "O"
        else:
            print("Player {} is not valid".format(player))
            sys.exit(-1)
        # self.show_board()
        return self.judge(row,col,player)

    def judge(self, row, col, player):
        symbol = ""
        if player == 1:
            symbol = "X"
        elif player == 2:
            symbol = "O"
        else:
            assert False
        row_items = self.board[row]
        if all(elem == symbol for elem in row_items):
            return player
        column_items = [self.board[r][col] for r in range(0,self.size)]
        if all(elem == symbol for elem in column_items):
            return player
        if row == col and \
           all(self.board[idx][idx] == symbol for idx in range(0,self.size)):
            return player
        if row == self.size - 1 - col and \
           all(self.board[idx][self.size-1-idx] == symbol for idx in range(0,self.size)):
            return player
        return 0
        
    def show_board(self):
        print(self.board)
        for i in range(self.size):
            for j in range(self.size):
                print("{} ".format(self.board[i][j]), end="")
            print()
        print()
        print("-" * 80)
        
