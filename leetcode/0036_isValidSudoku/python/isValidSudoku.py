from collections import Counter
BOARD_SIZE = 9
class Solution2(object):
    def isValidSudoku(self, board):
        verified_board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        ret = True
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = board[i][j]
                if self.isValidPos(verified_board, i, j, value):
                    verified_board[i][j] = value
                else:
                    return False
        return ret

    def isValidPos(self, verified_board, i, j, value):
        if (i,j) in [(2,2), (2,5), (2,8),(5,2), (5,5), (5,8),(8,2), (8,5), (8,8)]:
            subBox = self.getSubBox(verified_board, i, j, value)
            if subBox and not self.isValidList(subBox):
                print("i: {}, j:{}, subbox: {}, badsubbox ".format(i,j,subBox))                            
                return False
        elif value == ".":
            return True
        myrow = verified_board[i].copy()
        myrow[j] = value
        if not self.isValidList(myrow):
            print("i: {}, j:{}, bad row".format(i,j))            
            return False

        mycol = []
        for r in range(BOARD_SIZE):
            mycol.append(verified_board[r][j])
        mycol[i] = value
        if not self.isValidList(mycol):
            print("i: {}, j:{}, bad col".format(i,j))
            return False
        return True

    def isValidList(self, l):
        counter = Counter(l)
        keys = counter.keys()
        for k in keys:
            if k == ".":
                continue
            if int(k) < 0 or int(k) > BOARD_SIZE:
                return False
            if counter[k] > 1:
                return False
        return True

    def getSubBox(self, verified_board, i, j, value):
        if i < 2 or j < 2:
            return None
        subBox = []
        for k in range(3):
            sr = []
            for t in range(3):
                sr.append(verified_board[i-2+t][j-2+k])
            subBox.append(sr)
        subBox[-1][-1] = value
        return [el for row in subBox for el in row]
    
class Solution11(object):
    def isValidSudoku(self, board):
        verified_board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        ret = True
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                value = board[i][j]
                if self.isValidPos(verified_board, i, j, value):
                    verified_board[i][j] = value
                else:
                    return False
        return ret                

    def isValidPos(self, verified_board, i, j, value):
        if (i,j) in [(2,2), (2,5), (2,8),(5,2), (5,5), (5,8),(8,2), (8,5), (8,8)]:
            subBox = self.getSubBox(verified_board, i, j, value)
            print(subBox)            
            if not self.isValidList(subBox):
                print("bad subbox: {}, i:{}, j:{}".format(subBox, i, j))
                return False
        if value == ".":
            return True
        if value in verified_board[i]:
            print("bad row: i: {}, j: {}".format(i,j))
            return False
        mycol = []
        for r in range(BOARD_SIZE):
            mycol.append(verified_board[r][j])
        if value in mycol:
            print("bad col: i: {}, j: {}".format(i,j))            
            return False
        return True

    def getSubBox(self, verified_board, i, j, value):
        if i < 2 or j < 2:
            return None
        subBox = []
        for k in range(3):
            sr = []
            for t in range(3):
                sr.append(verified_board[i-2+t][j-2+k])
            subBox.append(sr)
        subBox[-1][-1] = value
        # print("subBox: {}, i: {}, j:{}".format(subBox, i, j))
        return [el for row in subBox for el in row]

    def isValidList(self, l):
        counter = Counter(l)
        keys = counter.keys()
        for k in keys:
            if k == ".":
                continue
            if int(k) < 0 or int(k) > BOARD_SIZE:
                return False
            if counter[k] > 1:
                return False
        return True
    

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        dices = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == '.': continue
                if e in rows[i] or e in cols[j] or e in dices[i//3][j//3]: return False
                rows[i].add(e)
                cols[j].add(e)
                dices[i//3][j//3].add(e)
                print("rows: {}".format(rows))
                print("cols: {}".format(cols))
                print("dices: {}".format(dices))                
        return True    
