from random import randint


class Board:
    def __init__(self, cols, rows):
        self.board = [['#'] * rows for _ in range(cols)]

    def print_board(self):
        for i in self.board:
            print(" ".join(i))
        

board_a = Board(14, 14)
board_b = Board(18, 18)
board_c = Board(22, 22)

def random_number():
    random = randint(0, len(board_c.board))
    return random

class Battleship:
    def __init__(self):
        self.length = None
        

    def render(self, board : Board):
        pass
        
        

class shipA(Battleship):
    def __init__(self):
        super(Battleship, self).__init__()
        self.length = 3

    def render(self):
        pass

class shipB(Battleship):
    def __init__(self):
        super(Battleship, self).__init__()
        pass

    def render(self):
        print("Bbbbb")

if __name__ == '__main__':
    print(board_c.print_board())
    print(random_number())