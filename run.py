from random import randint


class Game:
    def __init__(self, cols, rows):
        self.board = [['#'] * rows for _ in range(cols)]

    def print_board(self):
        for i in self.board:
            print(" ".join(i))
    
    def random_number(self):
        return randint(0, len(self.board)-1)
        

board_a = Game(14, 14)



class Battleship:
    def __init__(self):
        self.length = None
       
    def collision_check(self, game : Game):
        random_place = game.random_number()
        print(random_place)
        row = game.board[random_place]
        print(row)
        column = row[random_place]
        print(column)
        

    def render(self, game : Game):
        

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
    the_ship = Battleship()
    the_ship.collision_check(board_a)