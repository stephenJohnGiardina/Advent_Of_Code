from datetime import datetime


def challenge_1():
    number = original_number = obtain_number()
    for look_and_say in range(40):
        number = look_and_say_process(number)
    print("length of", original_number, "after 40 look and say processes = ", len(number))

def obtain_number():
    with open("2015/Day_10/input.txt", "r+") as input:
        return input.readline()

def look_and_say_process(number):
    new_number = ""
    number_of_copies = 1
    previous_digit = number[0]
    for digit in number[1:]:
        if digit == previous_digit:
            number_of_copies += 1
        else:
            new_number += str(number_of_copies) + previous_digit
            number_of_copies = 1
        previous_digit = digit
    new_number += str(number_of_copies) + previous_digit
    return new_number

def challenge_2():
    number = original_number = obtain_number()
    for look_and_say in range(50):
        number = look_and_say_process(number)
    print("length of", original_number, "after 50 look and say processes = ", len(number))
    pass

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 10")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    