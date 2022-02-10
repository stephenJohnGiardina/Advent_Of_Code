from datetime import datetime


def challenge_1():
    santas_list = obtain_santas_list()
    solution = (
        obtain_total_characters_in_literal(santas_list)
        - obtain_total_characters_in_memory(santas_list)
        )
    print("Number of characters in literal minus number of characters in memory =", solution)

def obtain_santas_list():
    santas_list = []
    with open("2015/Day_8/input.txt", "r+") as input:
        for line in input.readlines():
            santas_list.append(line.strip())
    return santas_list

def obtain_total_characters_in_literal(santas_list):
    total_characters_in_literal = 0
    for item in santas_list:
        total_characters_in_literal += len(item)
    return total_characters_in_literal

def obtain_total_characters_in_memory(santas_list):
    total_characters_in_memory = 0
    for item in santas_list:
        total_characters_in_memory += len(item) - obtain_amount_of_encoding_characters(item)
    return total_characters_in_memory

def obtain_amount_of_encoding_characters(item):
    amount_of_encoding_characters = 2
    current_char = ""
    hex_numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
    char_index = 0
    for char in item:
        if char == "\\":
            if current_char == "\\":
                amount_of_encoding_characters += 1
                current_char = ""
            elif current_char == "":
                current_char = "\\"
        if char == "\"" and char_index != len(item) - 1:
            if current_char == "\\":
                amount_of_encoding_characters += 1
                current_char = ""
        if char == "x":
            if current_char == "\\":
                if item[char_index + 1] in hex_numbers and item[char_index + 2] in hex_numbers:
                    amount_of_encoding_characters += 3
                    current_char = ""
        char_index += 1
    return amount_of_encoding_characters

def challenge_2():
    santas_list = obtain_santas_list()
    solution = (
        obtain_total_characters_in_encoded_string(santas_list)
        - obtain_total_characters_in_literal(santas_list)
        )
    print("Number of characters in encoded string minus number characters in literal =", solution)

def obtain_total_characters_in_encoded_string(santas_list):
    total_characters_in_encoded_string = 0
    for item in santas_list:
        total_characters_in_encoded_string += len(item) + obtain_amount_of_extra_characters_after_encoding(item)
    return total_characters_in_encoded_string

def obtain_amount_of_extra_characters_after_encoding(item):
    amount_of_extra_characters_after_encoding = 2
    for char in item:
        if char in ("\\", "\""):
            amount_of_extra_characters_after_encoding += 1
    return amount_of_extra_characters_after_encoding

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 8")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    