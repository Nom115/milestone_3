import random


class Player:
    def __init__(self, health, stamina, inventory):
        self.health = health
        self.stamina = stamina
        self.inventory = inventory


def get_player_fur():
    get_player_fur = input("What colour is your fur? A)Brown, B) White, C)Black").upper()
    while get_player_fur not in 'ABC':
        print("Not a valid choice, please select a correct option")
        get_player_fur = input("What colour is your fur? A)Brown, B) White, C)Black").upper()
    return get_player_fur


def RunGame():
    player = Player(100, 10, ["Sword of Destruction",])
    print("You are a prince, whose castle who has been taken over by the most evil, powerful cat-zard, Cattledoore. Now, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'.")
    player_fur = get_player_fur()
    

        
    while player.health > 0:
        print(player.health)
        
    print("")


if __name__ == "__main__":
    RunGame()
