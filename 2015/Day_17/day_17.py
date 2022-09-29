import os
from datetime import datetime


def challenge_1():
    containers = obtain_containers()
    possible_containers = obtain_possible_containers(containers)
    unique_possible_containers = list(set(map(lambda x: tuple(sorted(x)), possible_containers)))
    number_of_possible_containers = len(unique_possible_containers)
    print("Number of different combinations of containers that can exactly fit all 150 liters of eggnog =", number_of_possible_containers)
    return unique_possible_containers

def obtain_containers():
    containers = []
    with open(os.path.join("2015", "Day_17", "input.txt"), "r+") as input:
        for line_number, line in enumerate(input.readlines()):
            containers.append((int(line), line_number))
    return containers

def obtain_possible_containers(containers, current_containers=[]):
    if sum(list(map(lambda x: x[0], current_containers))) == 150:
        return [current_containers]
    possible_containers = []
    for container_index, container in enumerate(containers):
        if sum(list(map(lambda x: x[0], current_containers))) + container[0] <= 150:
            new_containers = containers[:container_index] + containers[container_index + 1:]
            possible_containers += obtain_possible_containers(new_containers, current_containers + [container])
    return possible_containers

def challenge_2(unique_possible_containers):
    minimum_number_of_containers = float("inf")
    number_of_minimum_number_of_containers = 1
    for unique_possible_container in unique_possible_containers:
        if len(unique_possible_container) < minimum_number_of_containers:
            number_of_minimum_number_of_containers = 1
            minimum_number_of_containers = len(unique_possible_container)
        elif len(unique_possible_container) == minimum_number_of_containers:
            number_of_minimum_number_of_containers += 1
    print("Number of different ways to fit exactly 150 liters of eggnog using the minimum number of containers =", number_of_minimum_number_of_containers)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 17")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    unique_possible_containers = challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2(unique_possible_containers)
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
