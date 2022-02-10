import os
from datetime import datetime


def challenge_1():
    lantern_fish = obtain_lantern_fish()
    
    for day in range(80):
        lantern_fish = wait_day(lantern_fish)
        
    print(len(lantern_fish))

def obtain_lantern_fish():
    with open(os.path.join("2021", "Day_6", "input.txt"), "r+") as input:
        return list(map(lambda x: int(x), input.readline().split(",")))

def wait_day(lantern_fish):
    new_lantern_fish = []
    birthing_fish = 0
    for fish in range(len(lantern_fish)):
        if lantern_fish[fish] == 0:
            birthing_fish += 1
            new_lantern_fish.append(6)
        else:
            new_lantern_fish.append(lantern_fish[fish] - 1)
    
    for new_fish in range(birthing_fish):
        new_lantern_fish.append(8)
    
    return new_lantern_fish

def challenge_2():
    lantern_fish = obtain_lantern_fish_memo()
    
    for day in range(256):
        lantern_fish = wait_day_memo(lantern_fish)
        
    print(obtain_number_of_fish(lantern_fish))

def obtain_lantern_fish_memo():
    lantern_fish_memo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(os.path.join("2021", "Day_6", "input.txt"), "r+") as input:
        lantern_fish_list = list(map(lambda x: int(x), input.readline().split(",")))
    
    for lantern_fish in lantern_fish_list:
        lantern_fish_memo[lantern_fish] += 1
    return lantern_fish_memo

def wait_day_memo(lantern_fish):
    new_fish = lantern_fish[0]
    
    lantern_fish[0] = lantern_fish[1]
    lantern_fish[1] = lantern_fish[2]
    lantern_fish[2] = lantern_fish[3]
    lantern_fish[3] = lantern_fish[4]
    lantern_fish[4] = lantern_fish[5]
    lantern_fish[5] = lantern_fish[6]
    lantern_fish[6] = lantern_fish[7] + new_fish
    lantern_fish[7] = lantern_fish[8]
    lantern_fish[8] = new_fish
    
    return lantern_fish

def obtain_number_of_fish(lantern_fish):
    number_of_fish = 0
    for fish in lantern_fish:
        number_of_fish += fish
    return number_of_fish

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 6")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
