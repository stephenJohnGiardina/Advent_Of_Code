import os
from datetime import datetime


def challenge_1():
    aunt_sues = obtain_aunt_sues()
    target_aunt_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for aunt_sue in aunt_sues:
        if aunt_sue[1][1] == target_aunt_sue[aunt_sue[1][0]]:
            if aunt_sue[2][1] == target_aunt_sue[aunt_sue[2][0]]:
                if aunt_sue[3][1] == target_aunt_sue[aunt_sue[3][0]]:
                    aunt_id = aunt_sue[0]
                    break
    print("ID of Aunt Sue that gave you your gift =", aunt_id)

def obtain_aunt_sues():
    aunt_sues = []
    with open(os.path.join("2015", "Day_16", "input.txt"), "r+") as input:
        for line in input.readlines():
            aunt_sues.append(
                (
                    int(line.split(" ")[1][:-1]),
                    (line.split(" ")[2][:-1], int(line.split(" ")[3][:-1])),
                    (line.split(" ")[4][:-1], int(line.split(" ")[5][:-1])),
                    (line.split(" ")[6][:-1], int(line.split(" ")[7]))
                )
            )
    return aunt_sues

def challenge_2():
    aunt_sues = obtain_aunt_sues()
    target_aunt_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    for aunt_sue in aunt_sues:
        if real_aunt_sue(aunt_sue, target_aunt_sue):
            aunt_id = aunt_sue[0]
            break
    print("ID of real Aunt Sue that gave you your gift =", aunt_id)

def real_aunt_sue(aunt_sue, target_aunt_sue, current_property=1):
    if current_property == 4:
        return True
    if aunt_sue[current_property][0] in ("cats", "trees"):
        if aunt_sue[current_property][1] > target_aunt_sue[aunt_sue[current_property][0]]:
            return real_aunt_sue(aunt_sue, target_aunt_sue, current_property + 1)
        return False
    elif aunt_sue[current_property][0] in ("pomeranians", "goldfish"):
        if aunt_sue[current_property][1] < target_aunt_sue[aunt_sue[current_property][0]]:
            return real_aunt_sue(aunt_sue, target_aunt_sue, current_property + 1)
        return False
    else:
        if aunt_sue[current_property][1] == target_aunt_sue[aunt_sue[current_property][0]]:
            return real_aunt_sue(aunt_sue, target_aunt_sue, current_property + 1)
        return False

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 16")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
