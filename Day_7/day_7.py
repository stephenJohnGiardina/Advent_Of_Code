from datetime import datetime


def challenge_1():
    crabs = obtain_crabs()
    max_crabs = max(crabs)

    fuel_values = []

    for crab_location in range(max_crabs + 1):
        fuel_values.append(find_fuel(crab_location, crabs))

    print(min(fuel_values))

def obtain_crabs():
    with open("Day_7/input.txt", "r+") as input:
        return list(map(lambda x: int(x), input.readline().split(",")))

def find_fuel(crab_location, crabs):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab_location - crab)
    return fuel

def challenge_2():
    crabs = obtain_crabs()
    max_crabs = max(crabs)

    fuel_values = []

    for crab_location in range(max_crabs + 1):
        fuel_values.append(find_fuel_non_constant(crab_location, crabs))

    print(min(fuel_values))

def find_fuel_non_constant(crab_location, crabs):
    fuel = 0
    for crab in crabs:
        current_fuel = 0
        for current_movement in range(abs(crab_location - crab)):
            current_fuel += current_movement + 1
        fuel += current_fuel
    return fuel

if __name__ == "__main__":
    print("Starting Challenges for Day 7")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
