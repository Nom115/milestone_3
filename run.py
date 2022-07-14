import random


class Player:
    def __init__(self, health, stamina, inventory):
        self.health = health
        self.stamina = stamina
        self.inventory = inventory

def RunGame():
    player = Player(100, 10, ["Sword of Destruction",])

    print(player.health)
    print(player.inventory)


if __name__ == "__main__":
    RunGame()
