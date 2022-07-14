import random
import time

# Player Class
class Player:
    def __init__(self, health, stamina, inventory, fur, party):
        self.health = health
        self.stamina = stamina
        self.inventory = inventory
        self.fur = fur
        self.party = party

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


# Function to allow player to chose the direction.
def get_player_direction():
    direction = {
        "A": "The armoury",
        "B": "The tavern",
        "C": "The dungeon",
        "D": "The castle",
    }
    player_direction = input(
        "Where would you like to go? \n A) The armoury \n B) The tavern \n C) The dungeon \n D) The Castle\n"
    ).upper()
    while player_direction not in "ABCD":
        print("Not a valid choice, please select a correct option")
        player_direction = input(
            "Where would you like to go? \n A) The armoury \n B) The tavern \n C) The dungeon \n D) The Castle\n"
        ).upper()
    p_chosen_direction = direction[player_direction]

    return p_chosen_direction


# The main hub, the village, this function is for the player to get around.
def village():
    print("You walk into a village close to the castle in the dead of night.")
    time.sleep(1)
    print("To the West there is a shop called 'Yakobs Armoury'.")
    time.sleep(1)
    print("To the North there is a tavern with many revellers and patrons.")
    time.sleep(1)
    print(
        "To the East there is a sign, with many warning written in blood. The sign says,\n 'BEWARE\n The Dungeon of Neverending Torment\n This way'"
    )
    time.sleep(4)
    print(
        "The castle is not too far from here, if you wanted to, you could head there now."
    )
    time.sleep(2)
    p_chosen = get_player_direction()
    return p_chosen


# Weapon generator
def weapon_generator():
    prefix = {
        1: "Nemesis",
        2: "Emberling",
        3: "Soulflare",
        4: "Lament",
        5: "Dusksong",
        6: "Dreamshadow",
        7: "Flameward",
        8: "Crucifier",
        9: "Torrent",
        10: "Starlight",
    }


# Begin the adventure
def RunGame():
    player = Player(
        100,
        10,
        [],
        "Placeholder",
        [],
    )

    def the_armoury():
        pass

    def the_tavern():
        pass

    def the_dungeon():
        pass

    def the_castle():
        print("You walk into the castle")
        player.health = 0

    player.get_player_fur()
    print(player.fur)
    time.sleep(1)
    print(player.inventory)
    print(
        f"You are a prince, with {player.fur} fur, whose castle who has been taken over by the most evil, powerful cat-zard, Cattledoore. \n Now, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'."
    )
    time.sleep(0)

    while player.health > 0:
        village_choice = village()
        if village_choice == "The armoury":
            the_armoury()
        elif village_choice == "The tavern":
            the_tavern()
        elif village_choice == "The dungeon":
            the_dungeon()
        elif village_choice == "The castle":
            the_castle()

        print(player.health)

    print("You Died")


if __name__ == "__main__":
    RunGame()
