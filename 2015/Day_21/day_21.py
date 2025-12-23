import os
from datetime import datetime


class Fighter:
    def __init__(self, hp, attack_points, defense_points):
        self.hp = hp
        self.attack_points = attack_points
        self.defense_points = defense_points

    def attack(self, fighter: "Fighter"):
        damage = self.attack_points - fighter.defense_points
        fighter.hp -= (damage if damage > 0 else 1)


def challenge_1():
    hp, attack_points, defense_points, ITEM_SHOP = obtain_input()
    min_cost = float("inf")
    for weapon_name, weapon_cost, weapon_attack, weapon_defense in ITEM_SHOP["Weapons"]:
        for armor_name, armor_cost, armor_attack, armor_defense in ITEM_SHOP["Armor"]:
            for ring_index, (ring_1_name, ring_1_cost, ring_1_attack, ring_1_defense) in enumerate(ITEM_SHOP["Rings"]):
                for ring_2_name, ring_2_cost, ring_2_attack, ring_2_defense in ITEM_SHOP["Rings"][:ring_index] + ITEM_SHOP["Rings"][ring_index + 1:]:
                    cost = weapon_cost + armor_cost + ring_1_cost + ring_2_cost
                    attack = weapon_attack + armor_attack + ring_1_attack + ring_2_attack
                    defense = weapon_defense + armor_defense + ring_1_defense + ring_2_defense
                    boss = Fighter(hp, attack_points, defense_points)
                    player = Fighter(100, attack, defense)
                    while True:
                        player.attack(boss)
                        if boss.hp <= 0:
                            cost = cost
                            break
                        boss.attack(player)
                        if player.hp <= 0:
                            cost = float("inf")
                            break
                    if cost < min_cost:
                        min_cost = cost
    print(f"Min Cost = {min_cost}")


def obtain_input():
    with open(os.path.join("2015", "Day_21", "input.txt"), "r+") as input:
        hp, attack_points, defense_points = list(map(lambda x: int(x.strip().split()[-1]), input.readlines()))
    ITEM_SHOP = {
        "Weapons": [
            ("Dagger",        8,     4,       0),
            ("Shortsword",   10,     5,       0),
            ("Warhammer",    25,     6,       0),
            ("Longsword",    40,     7,       0),
            ("Greataxe",     74,     8,       0)
        ],
        "Armor": [
            ("Nothing",       0,     0,       0),
            ("Leather",      13,     0,       1),
            ("Chainmail",    31,     0,       2),
            ("Splintmail",   53,     0,       3),
            ("Bandedmail",   75,     0,       4),
            ("Platemail",   102,     0,       5)
        ],
        "Rings": [
            ("Nothing",       0,     0,       0),
            ("Damage +1",    25,     1,       0),
            ("Damage +2",    50,     2,       0),
            ("Damage +3",   100,     3,       0),
            ("Defense +1",   20,     0,       1),
            ("Defense +2",   40,     0,       2),
            ("Defense +3",   80,     0,       3)
        ]
    }
    return hp, attack_points, defense_points, ITEM_SHOP


def challenge_2():
    hp, attack_points, defense_points, ITEM_SHOP = obtain_input()
    max_cost = 0
    for weapon_name, weapon_cost, weapon_attack, weapon_defense in ITEM_SHOP["Weapons"]:
        for armor_name, armor_cost, armor_attack, armor_defense in ITEM_SHOP["Armor"]:
            for ring_index, (ring_1_name, ring_1_cost, ring_1_attack, ring_1_defense) in enumerate(ITEM_SHOP["Rings"]):
                for ring_2_name, ring_2_cost, ring_2_attack, ring_2_defense in ITEM_SHOP["Rings"][:ring_index] + ITEM_SHOP["Rings"][ring_index + 1:]:
                    cost = weapon_cost + armor_cost + ring_1_cost + ring_2_cost
                    attack = weapon_attack + armor_attack + ring_1_attack + ring_2_attack
                    defense = weapon_defense + armor_defense + ring_1_defense + ring_2_defense
                    boss = Fighter(hp, attack_points, defense_points)
                    player = Fighter(100, attack, defense)
                    while True:
                        player.attack(boss)
                        if boss.hp <= 0:
                            cost = 0
                            break
                        boss.attack(player)
                        if player.hp <= 0:
                            cost = cost
                            break
                    if cost > max_cost:
                        max_cost = cost
    print(f"Max Cost = {max_cost}")

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 21")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
