from random import randint


class Game:
    def __init__(self, cols, rows):
        self.board = [['#'] * rows for _ in range(cols)]

    def print_board(self):
        for i in self.board:
            print(" ".join(i))
    
    def random_number(self):
        return randint(0, len(self.board)-1)

    def random_direction(self):
        direction = randint(0,1)
        if direction == 0:
            return True
        else:
            return False

board_a = Game(14, 14)



class Battleship:
    def __init__(self):
        self.length = 3
       
    def collision_check(self, game : Game):
        random_col = game.random_number()
        random_row = game.random_number()
        direction = game.random_direction()
        print(random_col)
        print(random_row)
        row = game.board[random_row]
        print(row)
        column = row[random_col]
        print(column)
        positions = []
        for i in range(random_col, self.length):
            temp_pos = 0
            positions.append(column)
            temp_pos +=1
            print(row[random_col+temp_pos])
        
        if len(positions) != self.length:
            return "False"
        print(positions)



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