import json
from datetime import datetime


def challenge_1():
    document = obtain_document()
    sum_of_all_numbers = obtain_sum(document)
    print("The sum of all numbers found in JSON document = ", sum_of_all_numbers)

def obtain_document():
    with open("2015/Day_12/input.txt", "r+") as input:
        return json.load(input)

def obtain_sum(document, ignore_red=False):
    if isinstance(document, int):
        return document
    if isinstance(document, str):
        return 0
    sum_of_all_numbers = 0
    if isinstance(document, list):
        for item in document:
            sum_of_all_numbers += obtain_sum(item, ignore_red)
    if isinstance(document, dict):
        if ignore_red and "red" in document.values():
            return 0
        for item in document.values():
            sum_of_all_numbers += obtain_sum(item, ignore_red)
    return sum_of_all_numbers

def challenge_2():
    document = obtain_document()
    sum_of_all_numbers = obtain_sum(document, True)
    print("The sum of all numbers found in JSON document ignoring red = ", sum_of_all_numbers)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 12")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    