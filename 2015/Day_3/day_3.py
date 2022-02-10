from datetime import datetime


def challenge_1():
    directions = obtain_directions()
    current_x = 0
    current_y = 0
    visited_houses = {(current_x, current_y)}
    for direction in directions:
        if direction == ">":
            current_x += 1
        if direction == "<":
            current_x -= 1
        if direction == "^":
            current_y += 1
        if direction == "v":
            current_y -= 1
        visited_houses.add((current_x, current_y))
    print("Number of houses visited =", len(visited_houses))

def obtain_directions():
    with open("2015/Day_3/input.txt", "r+") as input:
        return input.readline()

def challenge_2():
    directions = obtain_directions()
    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0
    visited_houses = {(santa_x, santa_y)}
    turn = 0
    for direction in directions:
        if turn % 2 == 0:
            if direction == ">":
                santa_x += 1
            if direction == "<":
                santa_x -= 1
            if direction == "^":
                santa_y += 1
            if direction == "v":
                santa_y -= 1
            visited_houses.add((santa_x, santa_y))
        else:
            if direction == ">":
                robo_santa_x += 1
            if direction == "<":
                robo_santa_x -= 1
            if direction == "^":
                robo_santa_y += 1
            if direction == "v":
                robo_santa_y -= 1
            visited_houses.add((robo_santa_x, robo_santa_y))
        turn += 1
    print("Number of houses visited =", len(visited_houses))

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 3")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
