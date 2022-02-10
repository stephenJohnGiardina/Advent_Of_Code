from datetime import datetime


def challenge_1():
    strings = obtain_strings()
    number_of_nice_strings = 0
    for string in strings:
        if (
            contains_3_vowels(string)
            and has_consecutive_letters(string)
            and does_not_contain_bad_substring(string)
            ):
            number_of_nice_strings += 1
    print("Number of nice strings =", number_of_nice_strings)

def obtain_strings():
    strings = []
    with open("2015/Day_5/input.txt", "r+") as input:
        for line in input.readlines():
            strings.append(line.strip())
    return strings

def contains_3_vowels(string):
    vowel_count = 0
    for char in string:
        if char in ("a", "e", "i", "o", "u"):
            vowel_count +=  1
            if vowel_count == 3:
                return True
    return False

def has_consecutive_letters(string):
    for char_index in range(len(string) - 1):
        if string[char_index] == string[char_index + 1]:
            return True
    return False

def does_not_contain_bad_substring(string):
    for vowel in ("ab", "cd", "pq", "xy"):
        if vowel in string:
            return False
    return True

def challenge_2():
    strings = obtain_strings()
    number_of_nice_strings = 0
    for string in strings:
        if (
            contains_2_pairs(string)
            and contains_repeating_letter_with_one_letter_between(string)
            ):
            number_of_nice_strings += 1
    print("Number of nice strings =", number_of_nice_strings)

def contains_2_pairs(string):
    for char_index in range(len(string) - 1):
        pair = string[char_index] + string[char_index + 1]
        for inner_char_index in range(len(string) - 1):
            if inner_char_index in (char_index - 1, char_index, char_index + 1):
                continue
            inner_pair = string[inner_char_index] + string[inner_char_index + 1]
            if pair == inner_pair:
                return True
    return False

def contains_repeating_letter_with_one_letter_between(string):
    for char_index in range(len(string) - 2):
        if string[char_index] == string[char_index + 2]:
            return True
    return False

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 5")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
