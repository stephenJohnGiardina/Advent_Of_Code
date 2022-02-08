import hashlib
from datetime import datetime


def challenge_1():
    secret_key = obtain_secret_key()
    current_hash = obtain_md5_hash(secret_key)
    decimal_number = 1
    while True:
        current_hash = obtain_md5_hash(secret_key + str(decimal_number))
        if current_hash[:5] == "00000":
            break
        decimal_number += 1
    print("Hash with 5 leading zeros found. Hash value =", current_hash)
    print("Lowest decimal number =", decimal_number)

def obtain_secret_key():
    with open("2015/Day_4/input.txt", "r+") as input:
        return input.readline()

def obtain_md5_hash(secret_key):
    return hashlib.md5(secret_key.encode("utf-8")).hexdigest()

def challenge_2():
    secret_key = obtain_secret_key()
    current_hash = obtain_md5_hash(secret_key)
    decimal_number = 1
    while True:
        current_hash = obtain_md5_hash(secret_key + str(decimal_number))
        if current_hash[:6] == "000000":
            break
        decimal_number += 1
    print("Hash with 6 leading zeros found. Hash value =", current_hash)
    print("Lowest decimal number =", decimal_number)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 4")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    