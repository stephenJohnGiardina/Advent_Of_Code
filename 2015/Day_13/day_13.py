import os
from datetime import datetime


def challenge_1():
    guests = obtain_guests()
    happinesses_of_arrangements = obtain_happinesses_of_arrangements(guests)
    optimal_happiness = max(happinesses_of_arrangements)
    print("The total happiness of the optimal seating arrangement =", optimal_happiness)

class Guest:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, nieghbor, happiness_unit):
        self.neighbors[nieghbor.name] = (nieghbor, happiness_unit)

def obtain_guests():
    guests = {}
    with open(os.path.join("2015", "Day_13", "input.txt"), "r+") as input:
        for line in input.readlines():
            guest_name = line.split(" ")[0]
            if guest_name not in guests:
                guests[guest_name] = Guest(guest_name)
            neighbor_name = line.strip().split(" ")[-1][:-1]
            if neighbor_name not in guests:
                guests[neighbor_name] = Guest(neighbor_name)
            happiness_unit = int(line.split(" ")[3])
            if line.split(" ")[2] == "lose":
                happiness_unit *= -1
            guests[guest_name].add_neighbor(guests[neighbor_name], happiness_unit)
    return guests

def obtain_happinesses_of_arrangements(guests):
    names_of_guests = list(guests.keys())
    possible_arrangements = obtain_possible_arrangements(names_of_guests)
    happinesses_of_arrangements = []
    for arrangement in possible_arrangements:
        happinesses_of_arrangements.append(obtain_happiness_of_arrangement(guests, arrangement))
    return happinesses_of_arrangements

def obtain_possible_arrangements(guests, current_arrangement=[]):
    if len(guests) == 0:
        return [current_arrangement]
    arrangements = []
    guest_index = 0
    for guest in guests:
        new_guests = guests[0:guest_index] + guests[guest_index + 1:]
        new_arrangement = current_arrangement + [guest]
        arrangements += obtain_possible_arrangements(new_guests, new_arrangement)
        guest_index += 1
    return arrangements

def obtain_happiness_of_arrangement(guests, arrangement):
    happiness = 0
    guest_index = 0
    for guest in arrangement:
        if guest_index == 0:
            left_neighbor_hapiness = guests[guest].neighbors[arrangement[len(arrangement) - 1]][1]
            right_neighbor_happiness = guests[guest].neighbors[arrangement[guest_index + 1]][1]
        elif guest_index == len(arrangement) - 1:
            left_neighbor_hapiness = guests[guest].neighbors[arrangement[guest_index - 1]][1]
            right_neighbor_happiness = guests[guest].neighbors[arrangement[0]][1]
        else:
            left_neighbor_hapiness = guests[guest].neighbors[arrangement[guest_index - 1]][1]
            right_neighbor_happiness = guests[guest].neighbors[arrangement[guest_index + 1]][1]
        happiness += left_neighbor_hapiness + right_neighbor_happiness
        guest_index += 1
    return happiness

def challenge_2():
    guests = obtain_guests()
    guests["SELF"] = Guest("SELF")
    for guest in guests.keys():
        if guest == "SELF":
            continue
        guests["SELF"].add_neighbor(guests[guest], 0)
        guests[guest].add_neighbor(guests["SELF"], 0)
    happinesses_of_arrangements = obtain_happinesses_of_arrangements(guests)
    optimal_happiness = max(happinesses_of_arrangements)
    print("The total happiness of the optimal seating arrangement =", optimal_happiness)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 13")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
