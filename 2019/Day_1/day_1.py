import os
from datetime import datetime


def challenge_1():
    pass

def obtain_input():
    with open(os.path.join("2019", "Day_1", "input.txt"), "r+") as input:
        pass

def challenge_2():
    pass

if __name__ == "__main__":
    print("Starting Challenges for Year 2019 Day 1")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
