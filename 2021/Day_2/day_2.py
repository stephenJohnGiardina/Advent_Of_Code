import os
from datetime import datetime


def challenge_1():
    depth = 0
    length = 0
    with open(os.path.join("2021", "Day_2", "input.txt"), "r+") as input:
        for line in input.readlines():
            distance = int(line.split(" ")[1])
            if "forward" in line:
                length += distance
            if "down" in line:
                depth += distance
            if "up" in line:
                depth -= distance

    print(depth * length)

def challenge_2():
    depth = 0
    length = 0
    aim = 0
    with open(os.path.join("2021", "Day_2", "input.txt"), "r+") as input:
        for line in input.readlines():
            distance = int(line.split(" ")[1])
            if "forward" in line:
                length += distance
                depth += aim * distance
            if "down" in line:
                aim += distance
            if "up" in line:
                aim -= distance

    print(depth * length)

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 2")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
