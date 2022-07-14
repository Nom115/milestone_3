import random

from grpc import StreamUnaryMultiCallable

class Player:
    def __init__(self, health, stamina):
        self.health = health
        self.stamina = stamina

def RunGame():
    player = Player(100, 10)

    print(player.health)


if __name__ == "__main__":
    RunGame()
