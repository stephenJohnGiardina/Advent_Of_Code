def challenge_1():
    depth = 0
    length = 0
    with open("Day_2/input.txt", "r+") as input:
        for line in input.readlines():
            distance = int(line.split(" ")[1])
            if "forward" in line:
                length += distance
            if "down" in line:
                depth += distance
            if "up" in line:
                depth -= distance

    print(depth * length)

def challenge_2():
    depth = 0
    length = 0
    aim = 0
    with open("Day_2/input.txt", "r+") as input:
        for line in input.readlines():
            distance = int(line.split(" ")[1])
            if "forward" in line:
                length += distance
                depth += aim * distance
            if "down" in line:
                aim += distance
            if "up" in line:
                aim -= distance

    print(depth * length)

if __name__ == "__main__":
    challenge_1()
    challenge_2()
