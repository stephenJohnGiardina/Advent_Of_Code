import os
from datetime import datetime


def challenge_1():
    binary_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    number_of_lines = 0
    with open(os.path.join("2021", "Day_3", "input.txt"), "r+") as input:
        for line in input.readlines():
            number_of_lines += 1
            bits = line.strip()
            for bit in range(len(bits)):
                if bits[bit] == "1":
                    binary_data[bit] += 1
    
    gamma_rate = []
    epsilon_rate = []
    for number in binary_data:
        if number_of_lines - number > number_of_lines / 2:
            gamma_rate.append(0)
            epsilon_rate.append(1)
        if number_of_lines - number < number_of_lines / 2:
            gamma_rate.append(1)
            epsilon_rate.append(0)
    
    gamma_rate = int("".join(map(lambda x: str(x) ,gamma_rate)), 2)
    epsilon_rate = int("".join(map(lambda x: str(x) ,epsilon_rate)), 2)

    print(gamma_rate * epsilon_rate)

def challenge_2():
    with open(os.path.join("2021", "Day_3", "input.txt"), "r+") as input:
        binary_data = input.readlines()

    binary_data = list(map(lambda x: x.strip(), binary_data))

    O_rating = get_rating(binary_data.copy(), "O")
    CO2_rating = get_rating(binary_data.copy(), "CO2")

    print(O_rating * CO2_rating)

def get_rating(binary_data, rating_type):
    binary_index = 0
    while len(binary_data) > 1:
        most_common_digit = find_most_common_digit(binary_data, binary_index)
        if most_common_digit != False and rating_type == "CO2":
            if most_common_digit == "1":
                most_common_digit = "0"
            elif most_common_digit == "0":
                most_common_digit = "1"
        binary_data = filter_digits(binary_data, most_common_digit, binary_index, rating_type)
        binary_index += 1

    return int(binary_data[0], 2)

def find_most_common_digit(binary_data, index):
    ones = 0
    zeros = 0
    for number in binary_data:
        if number[index] == "1":
            ones += 1
        if number[index] == "0":
            zeros += 1
    
    if ones > zeros:
        return "1"
    elif zeros > ones:
        return "0"
    else:
        return False

def filter_digits(binary_data, digit, index, rating_type):
    new_binary_data = []
    if digit == False:
        if rating_type == "O":
            digit = "1"
        if rating_type == "CO2":
            digit = "0"
    for number in binary_data:
        if number[index] == digit:
            new_binary_data.append(number)

    return new_binary_data


if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 3")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
