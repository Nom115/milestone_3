from random import randint


class Board:
    def __init__(self, row, col):
        self.col = col
        self.row = row

    def print_board(self):
        board = [["#" for a in range(self.col)] for b in range(self.row)]
        for i in board:
            print(" ".join(i))
        

board_a = Board(14, 14)
board_b = Board(18, 18)
board_c = Board(22, 22)


class Battleship:
    def __init__(self):
        pass

    def render(self):
        pass

class shipA(Battleship):
    def __init__(self):
        super(Battleship, self).__init__()
        pass

    def render(self):
        print("Aaaaaa")

class shipB(Battleship):
    def __init__(self):
        super(Battleship, self).__init__()
        pass

    def render(self):
        print("Bbbbb")

if __name__ == '__main__':
    print(board_c.print_board())