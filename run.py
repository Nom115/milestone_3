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
            "What colour is your fur?\nA) Brown\nB) White\nC) Black \n"
        ).upper()
        while get_player_fur not in "ABC":
            print("Not a valid choice, please select a correct option")
            get_player_fur = input(
                "What colour is your fur?\nA) Brown\nB) White\nC) Black \n"
            ).upper()
        self.fur = p_fur[get_player_fur]


# Function to allow player to chose the direction.
def get_player_direction():
    direction = {
        "A": "The armoury",
        "B": "The dungeon",
        "C": "The castle",
    }
    player_direction = input(
        "Where would you like to go? \n A) The armoury \n B) The dungeon \n C) The Castle\n"
    ).upper()
    while player_direction not in "ABC":
        print("Not a valid choice, please select a correct option")
        player_direction = input(
            "Where would you like to go? \n A) The armoury \n B) The dungeon \n C) The Castle \n"
        ).upper()
    p_chosen_direction = direction[player_direction]

    return p_chosen_direction


# The main hub, the village, this function is for the player to get around.
def village():
    print("You walk into a village close to the castle in the dead of night.")
    time.sleep(1)
    print("To the West there is a shop called 'Yakobs Armoury'.")
    time.sleep(1)
    print(
        "To the East there is a sign, with many warnings written in blood. The sign says,\n 'BEWARE\n The Dungeon of Neverending Torment\n This way'"
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

    type_of_wep = {
        1: "Sword",
        2: "Axe",
        3: "Hammer",
        4: "Dagger",
        5: "Staff",
    }

    suffix = {
        1: "of the shadows",
        2: "of honor",
        3: "of the immortal",
        4: "of the depth",
        5: "of fury",
        6: "of the sun",
        7: "of the claw",
        8: "of the enigma",
        9: "of grace",
        10: "of horrors",
    }

    prefix_choice = random.randint(1, 10)
    type_choice = random.randint(1, 5)
    suffix_choice = random.randint(1, 10)
    weapon = f"{prefix[prefix_choice]}, {type_of_wep[type_choice]} {suffix[suffix_choice]}"
    return weapon


Level = 1
# Begin the adventure
def rungame():
    player = Player(
        100,
        10,
        [],
        "Placeholder",
        [],
    )
    print("Welcome to DUNGEONS AND KITTENS")
    time.sleep(4)
    input("press enter to start:")
    def the_armoury():
        print("Welcome to the armoury")
        stay = int(input("Would you like to browse my wares? 1) Yes, 2) No\n"))
        wares = []
        for i in range(3):
            wares.append(weapon_generator())
        while stay == 1:

            purchase = int(
                input(
                    f"Which would you like, 1) {wares[0]}, 2) {wares[1]}, 3) {wares[2]}, 4) Nothing?\n"
                )
            )
            soldout = "Sold Out"
            if purchase == 1:
                player.inventory.append(wares[0])
                wares[0] = soldout
            elif purchase == 2:
                player.inventory.append(wares[1])
                wares[1] = soldout
            elif purchase == 3:
                player.inventory.append(wares[2])
                wares[2] = soldout
            elif purchase == 4:
                break
            print(player.inventory)
            stay = int(input("Would you like to buy anything else? 1) Yes, 2) No\n"))


    def the_dungeon():
        global Level
        Level = Level + 1

        print("You walk into the dungeon")
        enemy_health = 100

        if Level > 1:
            enemy_health = enemy_health * Level
        if Level > 10:
            enemy_health = enemy_health * (Level * 1.5)
        print(f"You enter level {Level}")
        time.sleep(1)
        while enemy_health > 0:
            player_damage = random.randint(30, 60) + Level*1.2

            if len(player.inventory) > 0:
                if Level == 1:
                    player_damage = player_damage + 50
                elif Level > 1:
                    player_damage = player_damage + (50 * (Level * 0.6))

                print(
                    f"You attack, dealing {player_damage} damage, using {player.inventory[0]}"
                )
            else:
                print(f"You attack, dealing {player_damage} damage")
            time.sleep(2)
            enemy_health = enemy_health - player_damage
            enemy_damage = random.randint(10, 20)
            if Level > 5:
                enemy_damage = random.randint(40, 100)
            elif Level > 10:
                enemy_damage = random.randint(100, 100 + (Level * 1.5))
            if enemy_health > 0:
                print(f"The enemy attacks, and deals {enemy_damage} damage to you")
            time.sleep(2)
            player.health = player.health - enemy_damage
            if player.health < 0:
                print("You run away from the fight, and retreat to the village to heal")
                break

            print(f"You have {player.health} hp left, and your enemy has {enemy_health} hp left")
        
        print(
            "You return to the village after a deadly battle, knowing where to go next time to get to the next level of the dungeon"
        )
        time.sleep(2)
        if Level > 0:
            player.health = 100 * Level
        elif Level > 10:
            player.health = player.health + (100 * (Level ^1.2))
        print(f"You feel stronger, and your health is now {player.health}")
        time.sleep(3)
        if Level == 10:
            print(
            "You leave the dungeon with a new weapon, this might be exactly what you need to defeat Cattledoore, 'purrfect whisker of eternal nightmares and damnation jr the third'!"
            )
            time.sleep(5)
            player.inventory.append(
                "purrfect whisker of eternal nightmares and damnation jr the third"
            )
            print(
                "You now are wielding the 'purrfect whisker of eternal nightmares and damnation jr the third', and can enter the castle."
            )
            time.sleep(4)

    def the_castle():
        if "purrfect whisker of eternal nightmares and damnation jr the third" not in player.inventory:
            print(
                "You walk into the castle courtyard, and instantly get incinerated by Cattledoore's strong magic!"
            )
            player.health = 0
        else:
            cattledoore_health = 30000
            while cattledoore_health > 0:
                if len(player.inventory) > 2:
                    player_damage = random.randint(50*Level, 55*Level)
                else:
                    player_damage = random.randint(25*Level, 30*Level)
                print(f"You attack Cattledoore, and deal {player_damage}")
                time.sleep(2)
                cattledoore_health = cattledoore_health - player_damage
                cattledoore_damage = random.randint(0,10)
                if cattledoore_damage == 3:
                    print("Cattledoore does a super attack, dealing 150 damage.")
                    cattledoore_damage = 150
                player.health = player.health - cattledoore_damage
                print(f"You are hit for {cattledoore_damage} and have {player.health} hp left")
            print("Cattledoore is killed and you take back the crown. The kingdom is saved!")
            time.sleep(5)
            print("Or so you think")
            time.sleep(1)
            print("...")
            time.sleep(3)
            print("Cattledoore awakens and uses the souls of your people to instantly kill you")
            player.health = 0


    player.get_player_fur()
    time.sleep(1)
    print(
        f"You are a prince, with {player.fur} fur, whose castle has been taken over by the most evil, powerful cat-zard, Cattledoore.\nNow, Cattledoore is in possesion of all the catnip in Catnipdom, so you must go on a quest, to retake your kingdom and help your people, by finding the 'purrfect whisker of eternal nightmares and damnation jr the third'."
    )
    time.sleep(6)

    while player.health > 0:
        village_choice = village()
        if village_choice == "The armoury":
            the_armoury()
        elif village_choice == "The dungeon":
            the_dungeon()
        elif village_choice == "The castle":
            the_castle()

    print("You Died!")
    print(f"Score: {Level}")


if __name__ == "__main__":
    rungame()
