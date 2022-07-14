import random

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
            "What colour is your fur? A)Brown, B) White, C)Black"
        ).upper()
        while get_player_fur not in "ABC":
            print("Not a valid choice, please select a correct option")
            get_player_fur = input(
                "What colour is your fur? A)Brown, B) White, C)Black"
            ).upper()
        self.fur = p_fur[get_player_fur]


# Begin the adventure
def RunGame():
    player = Player(
        100,
        10,
        [
            "Sword of Destruction",
        ],
        "Placeholder",
    )
    player.get_player_fur()
    print(player.fur)
    print(
        "You are a prince, whose castle who has been taken over by the most evil, powerful cat-zard, Cattledoore. Now, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'."
    )

    while player.health > 0:
        print(player.health)
        player.health = player.health - random.randint(99, 100)
    print("")


if __name__ == "__main__":
    RunGame()
