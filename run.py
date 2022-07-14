import random


class Player:
    def __init__(self, health, stamina, inventory):
        self.health = health
        self.stamina = stamina
        self.inventory = inventory

def RunGame():
    player = Player(100, 10, ["Sword of Destruction",])
    print("You are a prince, whose castle who has been taken over by the most evil, powerful cat-zard, Cattledoore. Now, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'.")
    
    
    while player.health > 0:
        print(player.health)
        
    print("")


if __name__ == "__main__":
    RunGame()
