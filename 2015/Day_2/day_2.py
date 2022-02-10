from datetime import datetime


def challenge_1():
    presents = obtain_presents()
    total_wrapping_paper = 0
    for present in presents:
        total_wrapping_paper += obtain_amount_of_wrapping_paper(present)
    print("Total amount of wrapping paper needed =", total_wrapping_paper)

def obtain_presents():
    presents = []
    with open("2015/Day_2/input.txt", "r+") as input:
        for line in input.readlines():
            presents.append(list(map(lambda x: int(x), line.strip().split("x"))))
    return presents

def obtain_amount_of_wrapping_paper(present):
    side_1 = present[0] * present[1]
    side_2 = present[0] * present[2]
    side_3 = present[1] * present[2]
    surface_area = 2 * side_1 + 2 * side_2 + 2 * side_3
    slack = min(side_1, side_2, side_3)
    return surface_area + slack

def challenge_2():
    presents = obtain_presents()
    total_ribbon = 0
    for present in presents:
        total_ribbon += obtain_amount_of_ribbon(present)
    print("Total amount of ribbon needed =", total_ribbon)

def obtain_amount_of_ribbon(present):
    return obtain_perimeter_of_smallest_side(present) + obtain_volume_of_present(present)

def obtain_perimeter_of_smallest_side(present):
    perimeter_1 = 2 * present[0] + 2 * present[1]
    perimeter_2 = 2 * present[0] + 2 * present[2]
    perimeter_3 = 2 * present[1] + 2 * present[2]
    return min(perimeter_1, perimeter_2, perimeter_3)

def obtain_volume_of_present(present):
    return present[0] * present[1] * present[2]

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 2")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
