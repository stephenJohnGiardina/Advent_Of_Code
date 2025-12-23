import os
from datetime import datetime


def get_elf_factors(house_number):
    elf_factors = set()
    for elf in range(1, int((house_number ** 0.5) + 1)):
        if house_number % elf == 0:
            elf_factors.add(elf)
            elf_factors.add(house_number // elf)
    return elf_factors

def challenge_1():
    target_number_of_presents = obtain_input() // 10
    house_number = 1
    while True:
        number_of_presents = sum(get_elf_factors(house_number))
        if number_of_presents >= target_number_of_presents:
            print("Lowest house number =", house_number)
            return
        house_number += 1

def obtain_input():
    with open(os.path.join("2015", "Day_20", "input.txt"), "r+") as input:
        return int(input.read())

def get_elf_factors_2(house_number, max_visits):
    number_of_presents = 0
    for elf in range(1, max_visits):
            if (house_number / elf) % 1 == 0:
                number_of_presents += (house_number / elf) * 11
    return number_of_presents

def challenge_2():
    target_number_of_presents = obtain_input()
    house_number = 1
    while True:
        number_of_presents = get_elf_factors_2(house_number, 50)
        if number_of_presents >= target_number_of_presents:
            print("Lowest house number =", house_number)
            return
        house_number += 1

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 20")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
