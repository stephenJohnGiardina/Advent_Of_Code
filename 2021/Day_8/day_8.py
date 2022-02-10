import os
from datetime import datetime


def challenge_1():
    all_signals_and_digits = load_all_signals_and_digits()
    
    number_of_unique_digits = 0
    
    for signals_and_digits in all_signals_and_digits:
        for digit in signals_and_digits["digits"]:
            if len(digit) in (2, 3, 4, 7):
                number_of_unique_digits += 1

    print(number_of_unique_digits)

def load_all_signals_and_digits():
    all_signals_and_digits = []
    with open(os.path.join("2021", "Day_8", "input.txt"), "r+") as input:
        for line in input.readlines():
            signals, digits = list(map(lambda x: x.strip().split(), line.split("|")))
            all_signals_and_digits.append(
                {
                    "signals": list(map(lambda x: "".join(sorted(x)), signals)),
                    "digits": list(map(lambda x: "".join(sorted(x)), digits))
                    }
                )
    return all_signals_and_digits

def challenge_2():
    all_signals_and_digits = load_all_signals_and_digits()
    
    sum_of_all_digits = 0
    
    for signals_and_digits in all_signals_and_digits:
        numbers = {
            "5": [],
            "6": []
            }
        letters = {}
        for signal in signals_and_digits["signals"]:
            if len(signal) == 2:
                numbers[1] = signal
            if len(signal) == 3:
                numbers[7] = signal
            if len(signal) == 4:
                numbers[4] = signal
            if len(signal) == 5:
                numbers["5"].append(signal)
            if len(signal) == 6:
                numbers["6"].append(signal)
            if len(signal) == 7:
                numbers[8] = signal

        a = find_a(numbers)
        letters[a] = "a"

        c, f = find_c_and_f(numbers)
        letters[c] = "c"
        letters[f] = "f"

        b, d = find_b_and_d(numbers)
        letters[b] = "b"
        letters[d] = "d"

        g = find_e_and_g(numbers, letters, c)
        letters[g] = "g"

        current_number = ""
        for digit in signals_and_digits["digits"]:
            current_number += convert_seven_segment_display(digit, letters)

        sum_of_all_digits += int(current_number)
    
    print(sum_of_all_digits)

def find_a(numbers):
    seven = numbers[7]
    one = numbers[1]
    for letter in seven:
        if letter not in one:
            return letter    

def find_c_and_f(numbers):
    one = numbers[1]
    for number in numbers["6"]:
        if one[0] not in number or one[1] not in number:
            six = number
            for letter in ("a", "b", "c", "d", "e", "f", "g"):
                if letter not in six:
                    c = letter
            for letter in one:
                if letter != c:
                    f = letter
                    break

    return c, f

def find_b_and_d(numbers):
    four = numbers[4]
    one = numbers[1]
    b_and_d = []
    for letter in four:
        if letter not in one:
            b_and_d.append(letter)
    
    for seven_segment_display in numbers["6"]:
        if b_and_d[0] not in seven_segment_display or b_and_d[1] not in seven_segment_display:
            zero = seven_segment_display
            
    if b_and_d[0] not in zero:
        d = b_and_d[0]
        b = b_and_d[1]
    if b_and_d[1] not in zero:
        d = b_and_d[1]
        b = b_and_d[0]
        
    return b, d

def find_e_and_g(numbers, letters, c):
    for seven_segment_display in numbers["5"]:
        if c not in seven_segment_display:
            five = seven_segment_display

    for letter in ("a", "b", "c", "d", "e", "f", "g"):
        if letter not in five and letter != c:
            e = letter
            letters[e] = "e"

    for letter in ("a", "b", "c", "d", "e", "f", "g"):
        if letter not in letters:
            g = letter

    return g

def convert_seven_segment_display(seven_segment_display, letters):
    seven_segment_displays = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9"
        }
    new_seven_segment_display = ""
    for letter in seven_segment_display:
        new_seven_segment_display += letters[letter]
    return seven_segment_displays["".join(sorted(new_seven_segment_display))]

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 8")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
