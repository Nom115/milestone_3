import random

class Player:
    def __init__(self, health):
        self.health = health
        

def RunGame():
    player = Player(100)

    print(player.health)


if __name__ == "__main__":
    RunGame()
