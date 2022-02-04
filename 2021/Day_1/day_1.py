from datetime import datetime


def challenge_1():
    with open("2021/Day_1/input.txt", "r+") as input:
        greater_than_count = 0
        previous = False
        for line in input.readlines():
            if previous == False:
                previous = int(line)
                continue
            current = int(line)
            if current > previous:
                greater_than_count += 1
            previous = current
    print(greater_than_count)

def challenge_2():
    with open("2021/Day_1/input.txt", "r+") as input:
        depths = []
        for line in input.readlines():
            depths.append(int(line))
        greater_than_count = 0
        previous = False
        for index in range(len(depths)):
            sum_of_next_three = obtain_sum_of_next_three(depths, index)
            if sum_of_next_three == False:
                break
            if previous == False:
                previous = sum_of_next_three
                continue
            current = sum_of_next_three
            if current > previous:
                greater_than_count += 1
            previous = current

    print(greater_than_count)

def obtain_sum_of_next_three(depths, index):
    if index + 3 > len(depths):
        return False
    else:
        return depths[index] + depths[index + 1] + depths[index + 2]

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 1")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
