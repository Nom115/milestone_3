import random
import time

# Player Class
class Player:
    def __init__(self, health, stamina, inventory, fur):
        self.health = health
        self.stamina = stamina
        self.inventory = inventory
        self.fur = fur

    # Method to allow player to customize fur
    def get_player_fur(self):
        p_fur = {
            "A": "Brown",
            "B": "White",
            "C": "Black",
        }
        get_player_fur = input(
            "What colour is your fur? A)Brown, B) White, C)Black \n"
        ).upper()
        while get_player_fur not in "ABC":
            print("Not a valid choice, please select a correct option")
            get_player_fur = input(
                "What colour is your fur? A)Brown, B) White, C)Black \n"
            ).upper()
        self.fur = p_fur[get_player_fur]


def village():
    print("You walk into a village close to the castle in the dead of night.")
    time.sleep(1)
    print("To the West there is a shop called 'Yakobs Armoury'.")
    time.sleep(1)
    print("To the North there is a tavern with many revellers and patrons.")
    time.sleep(1)
    print(
        "To the East there is a sign, with many warning written in blood. The sign says, 'BEWARE\n The Dungeon of Neverending Torment\n This way'"
    )
    time.sleep(1)
    print(
        "The castle is not too far from here, if you wanted to, you could head there now."
    )
    time.sleep(1)
    player_direction = input(
        "Where would you like to go? \n A) The armoury \n B) The tavern \n C) The dungeon \n D) The Castle"
    )


# Begin the adventure
def RunGame():
    player = Player(
        100,
        10,
        [],
        "Placeholder",
    )
    player.get_player_fur()
    print(player.fur)
    time.sleep(1)
    print(
        f"You are a prince, with {player.fur} fur, whose castle who has been taken over by the most evil, powerful cat-zard, Cattledoore. \n Now, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'."
    )
    time.sleep(10)
    village()
    while player.health > 0:
        print(player.health)
        player.health = player.health - random.randint(99, 100)
    print("")


if __name__ == "__main__":
    RunGame()
