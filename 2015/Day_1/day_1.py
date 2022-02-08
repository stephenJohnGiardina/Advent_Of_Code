from datetime import datetime


def challenge_1():
    directions = obtain_directions()
    floor = 0
    for direction in directions:
        if direction == "(":
            floor += 1
        if direction == ")":
            floor -= 1

    print("Final floor =", floor)

def obtain_directions():
    with open("2015/Day_1/input.txt", "r+") as input:
        return input.readline()

def challenge_2():
    directions = obtain_directions()
    current_position = 1
    floor = 0
    for direction in directions:
        if direction == "(":
            floor += 1
        if direction == ")":
            floor -= 1
        if floor == -1:
            break
        current_position += 1

    print("Basement first reached at position", current_position)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 1")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    