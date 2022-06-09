from random import randint


class Game:
    def __init__(self, cols, rows):
        self.board = [['#'] * rows for _ in range(cols)]

    def print_board(self):
        for i in self.board:
            print(" ".join(i))
        


board_a = Game(14, 14)

def random_number():
    random = randint(0, len(board_a.board))
    return random

class Battleship:
    def __init__(self):
        self.length = None
        

    def render(self, board : Game):
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
    board_a.print_board()
    print(random_number())