from datetime import datetime


def challenge_1():
    password = obtain_password()
    next_password = obtain_next_password(password)
    print("The next password after password", password, "=", next_password)

def obtain_password():
    with open("2015/Day_11/input.txt", "r+") as input:
        return input.readline()

def obtain_next_password(password):
    possible_straights = []
    for code in range(97, 121):
        possible_straights.append(chr(code) + chr(code + 1) + chr(code + 2))
    possible_pairs = []
    for code in range(97, 123):
        possible_pairs.append(chr(code) + chr(code))

    password = increment_password(password, 7)
    while not valid_password(possible_straights, possible_pairs, password):
        password = increment_password(password, 7)

    return password

def increment_password(password, password_index):
    if password_index == len(password) - 1:
        new_password = ""
    else:
        new_password = password[password_index + 1:]
    current_index = password_index
    for char_index in range(password_index, -1, -1):
        current_index -= 1
        char = password[char_index]
        if char != "z":
            new_password = chr(ord(char) + 1) + new_password
            break
        else:
            new_password = "a" + new_password
    if current_index == -1:
        return new_password
    return password[:current_index + 1] + new_password

def valid_password(possible_straights, possible_pairs, password):
    return (
        has_three_straight(possible_straights, password)
        and has_no_i_o_or_l(password)
        and has_two_pairs(possible_pairs, password)
        )

def has_three_straight(straights, password):
    for straight in straights:
        if straight in password:
            return True
    return False

def has_no_i_o_or_l(password):
    return not ("i" in password or "o" in password or "l" in password)

def has_two_pairs(pairs, password):
    total_pairs = 0
    for pair in pairs:
        total_pairs += password.count(pair)
        if total_pairs >= 2:
            return True
    return False

def challenge_2():
    password = obtain_password()
    password = obtain_next_password(password)
    next_password = obtain_next_password(password)
    print("The next password after password", password, "=", next_password)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 11")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
