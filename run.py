from random import randint

class Board:
    def __init__(self, row, col):
        self.col = col
        self.row = row

    def print_board(self):
        board = [["~" for a in range(self.col)] for b in range(self.row)]
        for i in board:
            print(" ".join(i))
        

board_a = Board(14, 14)
board_b = Board(18, 18)
board_c = Board(22, 22)


print(board_c.print_board())
