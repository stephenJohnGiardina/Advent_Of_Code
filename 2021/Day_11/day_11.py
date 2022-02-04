from datetime import datetime


def challenge_1():
    octopuses = load_octopuses()
    
    octopus_flashes = 0

    for step in range(100):
        flashed_octopuses = []
        flash_octopuses(octopuses, flashed_octopuses)

        octopus_flashes += get_flash_amount(octopuses)

    print(octopus_flashes)

def load_octopuses():
    octopuses = []
    with open("2021/Day_11/input.txt", "r+") as input:
        for line in input.readlines():
            octopuses.append(list(map(lambda x: int(x), line.strip())))
    return octopuses

def flash_octopuses(octopuses, flashed_octopuses):
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            flash_octopus(octopuses, row, col, flashed_octopuses)

def flash_octopus(octopuses, row, col, flashed_octopuses):
    if (row, col) in flashed_octopuses:
        return
    octopus = octopuses[row][col]
    if octopus != 9 and (row, col) not in flashed_octopuses:
        octopuses[row][col] += 1
    else:
        octopuses[row][col] = 0
        flashed_octopuses.append((row, col))
        if row > 0:
            flash_octopus(octopuses, row - 1, col, flashed_octopuses)
            if col < len(octopuses[row]) - 1:
                flash_octopus(octopuses, row - 1, col + 1, flashed_octopuses)

        if row < len(octopuses) - 1:
            flash_octopus(octopuses, row + 1, col, flashed_octopuses)
            if col > 0:
                flash_octopus(octopuses, row + 1, col - 1, flashed_octopuses)

        if col > 0:
            flash_octopus(octopuses, row, col - 1, flashed_octopuses)
            if row > 0:
                flash_octopus(octopuses, row - 1, col - 1, flashed_octopuses)

        if col < len(octopuses[row]) - 1:
            flash_octopus(octopuses, row, col + 1, flashed_octopuses)
            if row < len(octopuses) - 1:
                flash_octopus(octopuses, row + 1, col + 1, flashed_octopuses)

def get_flash_amount(octopuses):
    octopus_flashes = 0
    for row in octopuses:
        for octopus in row:
            if octopus == 0:
                octopus_flashes += 1
    return octopus_flashes

def challenge_2():
    octopuses = load_octopuses()

    number_of_octopuses = len(octopuses) * len(octopuses[0])

    step = 0

    while get_flash_amount(octopuses) != number_of_octopuses:
        flashed_octopuses = []
        flash_octopuses(octopuses, flashed_octopuses)
        step += 1

    print(step)

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 11")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
